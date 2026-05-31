# ArduPilot Parameter Generator (`apgen`) — Build Plan

> Target runtime: local box (“GX10”), Python 3.11+.
> Status: planning complete, ready to build. Branch: `claude/ssh-gx10-gbqLn`.
> Location: `projects/ardupilot_param_gen/`.

---

## 1. Context — why this tool

ArduPilot tuning means managing a few hundred flight-controller parameters as `.param`
text files. The mature GUI tool **ArduPilot Methodic Configurator (AMC)** already owns
templated config flows, calibration, and log-based project creation — so this tool does
**not** rebuild AMC. `apgen` is the **headless / CLI / agent-friendly complement**: the
scriptable layer AMC’s GUI doesn’t provide. It **fetches** parameter metadata,
**scaffolds** a set for a chosen vehicle, **validates** a `.param` file against that
metadata, **diffs/merges** sets, and **uploads** a validated set to a flight controller
over MAVLink.

**Non-goals:** GUI, IMU/compass calibration flows, log-file project creation (AMC owns
those), XML value export (no consumer exists), QGC format (deferred — see below).

---

## 2. Verified ground truth (checked against live ArduPilot / pymavlink source, May 2026)

These were confirmed by reading the actual source via `raw.githubusercontent.com`
(the published `autotest.ardupilot.org` host is **blocked by this build container’s
network allowlist**, so live-artifact fetch only works on the GX10, not in web sessions).

**Confirmed**
- **Vehicles:** `{ArduCopter, ArduPlane, Rover, ArduSub, AntennaTracker, Blimp}` are the
  valid `--vehicle` directory names (`AP_Periph` is a peripheral, excluded). The published
  URL pattern is `https://autotest.ardupilot.org/Parameters/<Vehicle>/apm.pdef.json`.
- **Artifact:** `apm.pdef.json`, emitted by
  `Tools/autotest/param_metadata/jsonemit.py` with `json.dump(..., indent=2, sort_keys=True)`.
- **Upload:** `mavutil.param_set_send(name, value, parm_type=None)` (defaults to
  `MAVLINK_TYPE_FLOAT`); the FC echoes a `PARAM_VALUE` back. `PARAM_SET` sets, `PARAM_VALUE`
  is the readback — **we** must write the set→ack→re-read confirm loop; pymavlink does not
  auto-confirm.

**Corrections that drive the data model** (do not trust a flat-map assumption)
- The JSON is **nested**, not a flat param map:
  ```json
  { "json": { "version": 0 },
    "<GroupName>": { "<PARAM_NAME>": { ...fields... } } }
  ```
  `parser.py` must skip the `"json"` meta key and flatten every group → param.
- **Mixed field-name casing** (real gotcha): the emitter lowercases/renames
  `displayName`, `description`, `user`, but leaves `Range`, `Values`, `Bitmask`, `Units`,
  `Increment`, `ReadOnly`, `Calibration`, `RebootRequired`, `Volatile`, `Vector3Parameter`
  in PascalCase. → pydantic models need explicit field **aliases**.
- **`Range` values are strings:** `{"low": "0", "high": "100"}`. `Values`/`Bitmask` are
  `{"<code-str>": "description"}`. Parse defensively (metadata can be messy: stray spaces in
  value codes, typo’d `user` levels).
- **Full known param fields:** `Description, DisplayName, Values, Range, Units, Increment,
  User, RebootRequired, Bitmask, Volatile, ReadOnly, Calibration, Vector3Parameter`.
  `User ∈ {Standard, Advanced}`.

---

## 3. Locked decisions

| Decision | Choice |
|---|---|
| First templates | **Copter 5in FPV** + **Plane fixed-wing** |
| Metadata sourcing | **Offline default** (vendored `apm.pdef.json` fixture); `--online` opt-in (works on GX10, blocked in web container) |
| QGC `.params` format | **Deferred** — leave a clean adapter seam in `reader`/`writer`, do not build now |
| Upload safety | **Skip `ReadOnly`/`Calibration` params by default; `--force` to override** |

### Upload safety, explained
- **Calibration params** (`COMPASS_OFS_*`, `INS_ACCOFFS_*`, …) are values the FC *measures*
  during calibration — unique to that physical board/sensors.
- **ReadOnly params** are ones firmware does not want overwritten.
- Blindly uploading a full `.param` file containing these can stamp one board’s calibration
  onto another and quietly break the vehicle. So `upload` **skips them by default** and only
  sets them when `--force` is passed.

---

## 4. Architecture

```
projects/ardupilot_param_gen/
├── pyproject.toml
├── core/
│   ├── metadata/
│   │   ├── fetcher.py      # GET apm.pdef.json per vehicle; on-disk cache + offline default
│   │   ├── model.py        # pydantic: ParamDef, ParamSet, VehicleMeta (with aliases)
│   │   └── parser.py       # parse nested .pdef.json -> flat ParamDef objects
│   ├── paramfile/
│   │   ├── reader.py       # parse .param text (NAME,VALUE / NAME VALUE, # comments)
│   │   └── writer.py       # emit .param (optional trailing "# reason"); QGC seam = TODO
│   ├── validate/
│   │   └── validator.py    # bounds, enum, bitmask, read-only, unknown-name, cross-field
│   ├── merge/
│   │   └── merger.py       # base + overlay merge, conflict policy
│   ├── upload/
│   │   └── mav.py          # pymavlink PARAM_SET + PARAM_VALUE readback confirm
│   └── templates/
│       ├── README.md
│       ├── copter_5in_fpv.param
│       └── plane_fixedwing.param
├── cli/
│   └── main.py             # click app; subcommands below
├── docs/
│   └── usage.md
└── tests/
    ├── fixtures/           # checked-in apm.pdef.json sample + sample .param files
    ├── test_fetcher.py     # uses fixture, network mocked
    ├── test_parser.py
    ├── test_reader_writer.py
    ├── test_validator.py
    ├── test_merger.py
    └── test_mav.py         # mock mavlink connection
```

---

## 5. CLI surface

- `apgen fetch <vehicle> [--firmware TAG] [--online]` — download/cache metadata (offline default).
- `apgen init <vehicle> [--template NAME] [-o out.param]` — scaffold a `.param` set.
- `apgen validate <file.param> --vehicle <V> [--firmware TAG]` — lint against metadata.
- `apgen merge <base.param> <overlay.param> [-o out.param] [--on-conflict overlay|base|error]`
- `apgen diff <a.param> <b.param> [--json]` — human-readable + machine diff.
- `apgen upload <file.param> --port <conn> [--dry-run] [--force]` — `PARAM_SET` + readback confirm.
- `apgen template list | show <NAME>` — manage value templates.
- `apgen docs <file.param> --vehicle <V> [-o table.md]` — annotated table (jinja2 + tabulate).

(No `edit` command — editing a `.param` is a plain text edit, not this tool’s job.)

---

## 6. Workflow

```
fetch metadata ──► init (template) ──► [user edits .param in $EDITOR] ──► validate
                                                                            │
                                              merge base+overlay ───────────┤
                                                                            ▼
                                          upload (PARAM_SET → PARAM_VALUE readback ack)
```

---

## 7. Dependencies

| Keep | Why |
|---|---|
| `click` | CLI |
| `pydantic` | metadata + set models, clean validation errors |
| `rich` | tables / progress |
| `requests` | fetch `.pdef.json` (online mode only) |
| `pymavlink` | the only correct way to do `PARAM_SET` / `PARAM_VALUE` readback |
| `jinja2` | docs output |
| `tabulate` | docs tables |
| `pytest` | tests |

**Dropped:** `jsonschema` (pydantic covers it), `pandas` (overkill for ~hundreds of pairs),
`semver` (AP tags like `Copter-4.5.7` aren’t semver — use `packaging.version` or a tiny
comparator), `loguru` (stdlib `logging` is enough).

---

## 8. Build sequence (milestones — each independently testable)

1. **Scaffold** — `pyproject.toml`, package skeleton, `click` app stub, pytest wiring.
2. **Metadata core** — `model.py` (pydantic with aliases), `parser.py` (nested flatten,
   skip `"json"`), `fetcher.py` (offline default + cache + `--online`). Ship a checked-in
   trimmed `apm.pdef.json` fixture (Copter + Plane subset). → `test_parser`, `test_fetcher`.
3. **Param files** — `reader.py` / `writer.py` (`NAME,VALUE` / `NAME VALUE`, `#` comments,
   optional `# reason`); QGC seam left as TODO. → `test_reader_writer`.
4. **Validate** — bounds / enum / bitmask / unknown-name / ReadOnly, `rich` report.
   → `test_validator`.
5. **Merge + diff** — `--on-conflict overlay|base|error`, `--json`. → `test_merger`.
6. **Templates** — `copter_5in_fpv.param` + `plane_fixedwing.param` with documented
   `# reason` lines; wire `init` / `template` commands.
7. **Upload** — `mav.py` `PARAM_SET` → `PARAM_VALUE` readback, `--dry-run`,
   ReadOnly/Calibration skip + `--force`. → `test_mav` (mocked link).
8. **Docs** — `apgen docs` (jinja2 + tabulate) + `usage.md`.

Everything is testable **offline** against the fixture; `--online` and real MAVLink are only
exercised on the GX10 (open egress). The web container can verify source facts via GitHub
raw but cannot reach `autotest.ardupilot.org` or a live flight controller.

---

## 9. Verification checklist (do while coding)

- [ ] Re-confirm `apm.pdef.json` URL pattern + vehicle list on the GX10 by fetching one live
      (web container is blocked; use the checked-in fixture there).
- [ ] Parse defensively for messy metadata (stray spaces in value codes, typo’d user levels).
- [ ] Confirm `pymavlink` `param_set_send` + `PARAM_VALUE` readback loop against a real or
      SITL flight controller on the GX10.
- [ ] If/when QGC support is un-deferred: verify the exact 4-column header
      (`VEHICLE_ID COMPONENT_ID NAME VALUE TYPE`) before implementing.
