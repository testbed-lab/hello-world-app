# C-UAS Site Selection Framework

**Working document — v3 draft**
**Audience:** Military and law enforcement planners
**Status:** Framework settled in structure; several inputs unverified (see §9)
**Last updated:** 31 July 2026

---

## 1. Purpose and scope

A repeatable method for evaluating a location — and for improving one you already
hold — against the unmanned aircraft system threat.

**Two site classes are covered:**

| Class | Examples |
|---|---|
| **A — Small / urban site** | Off-base billeting, protective-detail residence, safe house, temporary urban command post or observation post |
| **B — Fixed site / installation** | Military installation, correctional facility, large-scale public event venue, critical infrastructure site |

**Two decisions are supported**, using the same axes:

- **Select** — where do we go? (one-time, high leverage, rarely available)
- **Improve** — what do we do with where we are? (continuous, modest cost, applies to almost everyone)

Score the same six axes twice: once as *what does this site give me*, once as
*what can I buy back*.

---

## 2. Threat model — sort before you score

Adapted from IPB. Plan against the most likely; branch against the most dangerous.

### Most Likely (MLCOA)

You are not the target. You are a bystander, an observation subject, or downstream
of someone else's target.

| Threat | Documented frequency |
|---|---|
| Nuisance / hobbyist overflight | FAA: 100+ reports near airports monthly |
| Deliberate surveillance, casing | CBP: 34,682 flights within 500 m of the SW border, FY2025 |
| Contraband delivery | BOP: 479 prison incidents in 2024, up from 23 in 2018 (~20x in six years) |
| Unattributed incursion over sensitive sites | 350+ incursions at ~100 US installations in 2024; Langley AFB, 17 nights, forced F-22 relocation |
| Second-order infrastructure loss | PA substation 2020 (modified DJI Mavic 2); Nashville C-4 plot, FBI arrest Nov 2024 |

### Most Dangerous (MDCOA)

**Pre-positioned close-launch — the Spiderweb model.** 1 June 2025: 117 FPV drones
concealed in modified cabins on flatbed trucks, driven deep into Russia, launched
remotely against five airbases including Belaya in Siberia. 18 months of preparation.
~10–13 aircraft destroyed by independent assessment (41 claimed), ~$7bn damage.

**Planning consequence:** raw standoff distance is close to meaningless. The launch
point is wherever a vehicle can park. The replacement variable is *what can loiter
within 1–2 km unremarked* — a human-terrain question, not a terrain question.

### Interdiction (third profile)

Contraband delivery to correctional facilities. Highest-frequency documented threat
in the dataset, explicitly named in SAFER SKIES. Different problem shape: delivery,
not attack. SURVIVE and SUSTAIN barely matter; FIND, SEE, and STOP are everything.

---

## 3. Authority gate — assess first

**Authority is a site-selection variable, not a background constraint.** Two otherwise
identical sites score differently if one falls inside a covered-facility designation
and the other does not. Authority determines which axes are even live.

| Band | Basis | STOP available? |
|---|---|---|
| **Full mitigation** | DoD (10 USC 130i); DHS / DOJ (6 USC 124n); DOE | Yes |
| **SAFER SKIES certified** | FY2026 NDAA; implementing rule 6 July 2026 | Yes, within scope |
| **Detect-and-report only** | Uncertified SLTT — the majority today | **No** |

**10 USC 130i covered facilities/assets** are tied to specific missions: nuclear
deterrence, missile defense, national security space, POTUS/VPOTUS protection, air
defense of the US, combat support agencies, SOF, high-yield explosives production or
transport, Major Test Range and Test Facility Base.

**6 USC 124n** — DHS and DOJ designated covered facilities. Sunset extended to
1 Oct 2030; amended by FY2026 NDAA (P.L. 119-60).

**SAFER SKIES Act** (FY2026 NDAA) extends mitigation authority to state, local,
tribal, territorial law enforcement and correctional agencies against a "credible
threat" to people, facilities, large-scale public events, critical infrastructure,
and correctional institutions.

> **Certification bottleneck.** SLTT authority is gated behind a centralized federal
> certification process that reportedly cannot scale to thousands of agencies. Plan
> for detect-and-report as the default posture until certification is in hand.

**JIATF 401 role:** SecDef, acting through JIATF 401, must ensure that for each covered
facility where C-UAS operations are necessary, administrative actions for effective use
of those authorities are complete, including training policies.

**Privacy overlay (LE sites):** detection sensors raise civil-liberties exposure the
military case does not have. Governing reference is 401's companion publication,
*Counter-UAS Operations: Safeguarding Freedoms and Preserving Privacy*.

---

## 4. The spine — six axes

Each axis breaks a link in the adversary's chain.

| Axis | Adversary's question | Your counter |
|---|---|---|
| **FIND** | Can I locate it? | Records footprint, signature, EMCON |
| **REACH** | Can I get a launcher in range? | Launch geometry, approach control, standoff |
| **SEE** | *(yours)* Do I get usable warning? | Detection geometry, human terrain |
| **STOP** | Can they defeat me? | Effectors — authority-gated |
| **SURVIVE** | Does a hit accomplish anything? | Overhead cover, dispersion, construction |
| **SUSTAIN** | *(yours)* Can I continue after? | Utilities, medical, resupply, continuity |

Maps onto the JIATF 401 **Five Ds** (Detect → SEE; Deny → REACH; Disrupt/Defeat →
STOP; Discipline → FIND) while adding the two things doctrine leaves implicit:
**SURVIVE** and **SUSTAIN**.

The 401 **Four Ps** (person, platform, process, payload) characterize the threat and
feed REACH and SURVIVE.

### Relationship to JIATF 401 "Harden, Obscure, Perimeter" (HOP)

The 401 *Guide for Physical Protection of Critical Infrastructure* organizes physical
protection around **HOP**. This framework does not compete with HOP — it extends it.

| HOP element | Maps to |
|---|---|
| **Harden** | SURVIVE (and STOP — netting serves both) |
| **Obscure** | FIND (terminal-discrimination half) |
| **Perimeter** | REACH + SEE |

HOP addresses the **Improve** decision only. It does not cover SUSTAIN, does not treat
the authority gate, and does not address **Select**. Present this framework as extending
HOP, not as an alternative to it.

**Distinction worth preserving — FIND vs. Obscure:**

- **FIND** — can the adversary locate the site at all?
- **Obscure** — having located it, can they *identify and acquire the correct asset*?

These are different problems. Obscure is a terminal-phase discrimination problem, and it
is where decoys, visual clutter, and diversions do their work. Score both.

---

## 5. Framework A — Small / urban site

| Axis | What to assess |
|---|---|
| **FIND** | Records and lease footprint · overhead imagery of the structure · personnel pattern visibility · vehicle clustering · **EMCON** — cellular signal clusters are a documented detection vector used against Ukrainian command posts |
| **REACH** | Vehicle-accessible launch points within 1–2 km · elevated adjacent structures · standoff by threat class · who can loiter unremarked and for how long |
| **SEE** | Detection coverage — LOS-limited in clutter, often under 1 km · human terrain as primary sensor · realistic warning of 7–24 s against Group 1 |
| **STOP** | **Authority-gated.** Full → RF/GNSS effectors, *RF-linked threats only*. Gated → nets, screens, physical measures only. |
| **SURVIVE** | Masonry vs. frame construction · floors above vs. aperture accessibility · interior refuge with no exterior wall · sub-grade space |
| **SUSTAIN** | Utility redundancy · casualty evacuation time · comms resilience · continuity of the protective or collection mission |

### Weights

| Axis | MLCOA | MDCOA |
|---|---|---|
| SUSTAIN | **30%** | 15% |
| FIND | **25%** | 20% |
| SURVIVE | 15% | **30%** |
| REACH | 15% | **25%** |
| SEE | 10% | 10% |
| STOP | 5% | 0% |

### The floor paradox

No universal answer — resolve per site:

- Against **top-attack** (Group 3 / Shahed-class): want floors **above** you
- Against **window-entry FPV**: want **not** to be on an accessible floor with large apertures
- Ground floor loses both ways; top floor loses to top-attack
- Physics points at **middle floors of a masonry building with a windowless interior room**

---

## 6. Framework B — Fixed site / installation

| Axis | What to assess |
|---|---|
| **FIND** | **EMCON** — RF, cellular clusters, avoid HF (strong emissions, recognisable signature; if unavoidable, lowest power plus terrain masking) · decoy emitters placed away from the real site in believable configuration · thermal / acoustic / visual · **personnel count — signature scales exponentially with headcount** · vehicle clustering visible from overhead · public information about asset locations |
| **REACH** | Terrain overmatch — who holds, or could hold, dominating ground · vehicle-accessible launch points inside effective range · dead space and infiltration routes · perimeter standoff tiered by threat class · **extended perimeter as an active measure** — pushing the fenceline out strains UAS batteries, degrades control links, exposes operators, and widens the safety buffer (four effects from one measure, per 401 HOP) |
| **SEE** | LOS-driven **Area of Regard** defined before sensor placement · sensor siting vs. terrain masking · **required detection range = threat speed x (kill chain + margin)** |
| **STOP** | **Layer by cost tier — never trade expensive for cheap.** Passive/nets → EW (RF-linked threats only) → interceptors → guns → HPM for swarms. Kinetic defeat last, per Five Ds. |
| **SURVIVE** | Hardened and overhead cover · revetments and shelters · dispersion sized to effect radius · separation of like assets · displacement tempo |
| **SUSTAIN** | Power / water / fuel redundancy · resupply routes · casualty evacuation · mission continuity under degradation |

### Weights

| Axis | MLCOA | MDCOA | Interdiction |
|---|---|---|---|
| SEE | **25%** | 15% | **30%** |
| FIND | **25%** | 5% | 15% |
| STOP | 20% | 20% | **35%** |
| REACH | 15% | **25%** | 15% |
| SURVIVE | 10% | **30%** | 0% |
| SUSTAIN | 5% | 5% | 5% |

> The MDCOA column is **empirically validated**: after Spiderweb, Russia's actual
> response was hardened shelters (SURVIVE) and perimeter/vehicle control (REACH) —
> not more sensors.

---

## 7. Scoring mechanic

**1. Score each axis 1–5**, multiply by COA weight, sum. Run **every applicable COA
column** and keep the separate results. A site strong under MLCOA and catastrophic
under MDCOA is a different decision from one that is mediocre at both. Do not average
the COAs together.

**2. Veto conditions override the total.** A weighted sum can average away a fatal
flaw. Any of the following disqualifies a site regardless of score:

| Veto | Rationale |
|---|---|
| **Extensive dead space** that cannot be observed or denied | Wanat / Keating — see §8.11 Pattern D. Note this is *dead space*, not elevation: OP Bari Alai held the summit and was still overrun. |
| **Mutual support that exists on the site plan but not in current manning** | Camp Bastion — Tower 16 unmanned. See Pattern E. Verify against the manned configuration, not the design. |
| **Critical dependency sited outside the defensible perimeter** | Khe Sanh water, Wanat fuel, Zerok approach road. See Pattern F. |
| No egress — single route in and out | Choke point that no concealment fixes |
| No interior refuge without an exterior wall | No survivable position exists |
| Sustainment failure inside tolerance window | MLCOA harm is utility loss, not blast |
| Unacceptable on a **non-drone** hazard (flood, fire, casevac time, civil disorder) | Guards against over-fitting to one threat |
| **Hardening deferred because occupation is "temporary"** | Pattern A — the most persistent failure in the record, 1879 to 2012. If the plan depends on the site being temporary, the plan is the risk. |

> **Structural note.** The data center industry independently arrives at the same design: hazard and
> security factors act as **pass/fail screening filters**, while weighted scores are reserved for
> the primary drivers. Convergence from an unrelated domain is a good signal the veto mechanic is sound.

**3. Re-score on a cadence.** FPV range moved from 5–10 km to 25 km in roughly two
years; fiber-optic control defeated RF jamming outright. Every score has a shelf life.
Annual minimum, or on any observed capability shift.

**4. Define abandonment triggers at selection time**, not later. What observation makes
this site non-viable?

**5. "No acceptable site" is a valid output.** Relocation must be an allowed answer,
not a failure state.

**6. Score the transition, not just the end state.** Pattern H (§8.11): Wanat was attacked
*during* the repositioning window, while COP Bella was being disestablished and Wanat occupied
across the same three days. **The move between two adequately-scored sites is itself a period of
elevated risk** and must be planned as a distinct phase.

### What this framework cannot do

**It cannot detect organizational drift.** Patterns B and E in §8.11 — a forward position
administratively treated as a rear area, and mutual support that decays as manning thins — are
failures of the *institution*, not of the site. FSB Mary Ann (1971) and Nahal Oz (2023) were both
correctly assessed when selected. What decayed was the organization's understanding of what the
site was.

No site score captures this. It requires a **separate periodic posture review** asking: *does the
unit still believe this position is what it actually is?* Treat that as a companion process to
site scoring, not a criterion within it.

---

## 8. Reference data

### 8.1 Threat classes (DoD groups)

| Group | Weight | Altitude | Speed | Examples |
|---|---|---|---|---|
| 1 | <20 lb | <1,200 ft AGL | <100 kt | FPV, quadcopter |
| 2 | 21–55 lb | <3,500 ft AGL | <250 kt | Larger multirotor, small fixed-wing |
| 3 | 55–1,320 lb | <18,000 ft MSL | <250 kt | **Shahed-136 / Geran-2** |
| 4 | >1,320 lb | <18,000 ft | any | Reaper-class |
| 5 | >1,320 lb | >18,000 ft | any | Global Hawk-class |

### 8.2 Performance baseline

| | Shahed-136 | FPV quadcopter |
|---|---|---|
| Cruise speed | ~180 km/h (**50 m/s**); range 140–220 | up to ~150 km/h (**41.7 m/s**); attack runs often ~100 km/h |
| Altitude | ~1,000 m typical (20–2,000 m observed) | treetop to street level |
| RCS | ~0.01 m² | ~0.05 m² (DJI Phantom, X-band) |
| Range | ~1,000–1,800 km | 5–10 km legacy; **20–25 km** current; 30+ km fixed-wing |
| Warhead | 20–50 kg | ~0.3–3.5 kg |

Note the inversion: the Shahed has a **smaller RCS** than a quadcopter but is detected
much farther out, because it flies at 1,000 m in clear air while the FPV hugs clutter.
**Detection range is a function of geometry, not size.**

### 8.3 Engagement math

Kill chain — first detection to non-kinetic defeat: **15–40 seconds** under normal
conditions. Kinetic adds time; degraded or manual operation adds considerably more.

**Time to target:**

| Range | Shahed @ 50 m/s | FPV @ 41.7 m/s |
|---|---|---|
| 10 km | 3 min 20 s | 4 min 00 s |
| 5 km | 1 min 40 s | 2 min 00 s |
| 2 km | 40 s | 48 s |
| 1 km | 20 s | **24 s** |
| 500 m | 10 s | **12 s** |
| 300 m | 6 s | **7 s** |

**Margin = flight time − kill chain:**

| Scenario | Detection | Flight time | Margin (15 s) | Margin (40 s) |
|---|---|---|---|---|
| Shahed, open terrain | 10 km | 200 s | +185 s | +160 s |
| Shahed, terrain-masked | 2 km | 40 s | +25 s | **0 s — coin flip** |
| FPV, good radar | 3 km | 72 s | +57 s | +32 s |
| FPV, typical sUAS radar | 2 km | 48 s | +33 s | +8 s |
| FPV, cluttered / urban | 1 km | 24 s | +9 s | **−16 s — lost** |
| FPV, acoustic / visual only | 300 m | 7 s | **−8 s** | **−33 s — lost** |

**Minimum detection range required** = speed x (kill chain + margin):

| Threat | Break-even (40 s) | With 2x margin |
|---|---|---|
| Shahed @ 50 m/s | **2.0 km** | 4.0 km |
| FPV @ 41.7 m/s | **1.7 km** | 3.3 km |

Achievable detection: dedicated small-UAS radar 1–3 km; large phased-array claims
5–30 km. **Against FPV you are operating at or below break-even with typical sensors**,
before terrain takes its cut.

Radar horizon is **not** the binding constraint — a 10 m sensor against a 50 m target
still yields ~42 km. The limiter is **terrain masking and clutter**, which is a siting
variable.

### 8.4 Link type beats size

Size does not predict EW vulnerability. The **control and navigation link** does.

| Link type | Jamming effective? |
|---|---|
| RF-controlled | **Yes** |
| GNSS-dependent | Partial — degrading as CRPA anti-jam antennas proliferate |
| **Fiber-optic** | **No** — immune to jamming and to ambient RF noise |
| SATCOM | No |
| **Fully autonomous / AI** | **No** — no signal to jam |

Scale: by early 2026, 35+ Ukrainian manufacturers produce fiber-optic drones; Russian
adoption has reached **30–50% in some front-line units**. AI terminal guidance is a
targeted defeat of terminal jamming — the operator flies ingress, then hands off to AI
for the final ~500 m where jamming is heaviest.

**A Group 1 fiber-optic FPV is harder to defeat electronically than a Group 3 Shahed.**
Difficulty is close to inverted at the low end.

Only **HPM** (destroys electronics regardless of operating state) and **directed energy**
(physically damages airframe or sensors) affect fully autonomous systems.

### 8.5 Effectiveness by threat class

| Method | Grp 1 RF | Grp 1 fiber/auto | Grp 3 | Swarm |
|---|---|---|---|---|
| RF jamming | Good | **None** | Partial | Good if all RF |
| GNSS denial / spoof | Some | **None** | Degrading | Partial |
| Guns / direct fire | Short window | Short window | Good | Saturates |
| SAM (Patriot-class) | Absurd cost | Absurd cost | Works, ruinous | No |
| Interceptor drones | Emerging | Emerging | **>60%** | Numbers-limited |
| **HPM** | Yes | **Yes** | Yes | **Best** |
| Laser (HEL) | Yes | Yes | Yes | One at a time |
| Nets / entanglement | Partial | Partial | Too much mass | No |
| **Overhead cover** | **Yes** | **Yes** | **Yes** | **Yes** |
| **Dispersion / concealment** | **Yes** | **Yes** | **Yes** | **Yes** |

**The bottom two rows are the only measures effective across every column.** That is the
central argument for weighting passive measures heavily — and it is why the framework
survives the authority gate.

### 8.6 Cost exchange

| Option | Cost per engagement | Against | Ratio |
|---|---|---|---|
| Patriot PAC-3 | **~$4M** | Shahed @ $30–80k | **~50–130:1 losing** |
| Merops interceptor | ~$15,000 | Shahed | ~2–3:1 winning |
| Ukrainian autonomous interceptor | **~$3,500** | Shahed @ $40–80k | **~11–23:1 winning** |
| HPM (Epirus Leonidas) | Near-zero marginal | 49 drones dropped in 2 s | Overwhelming |

Shaheds hit their target **under 10% of the time** — irrelevant, because they are used
to saturate, clutter radar, and force defenders to expend expensive interceptors.

### 8.7 Effector by event type

| Event | Best answer | Why |
|---|---|---|
| Single surveillance overflight | Detection + signature discipline | Nothing to defeat; deny the collection |
| Single armed Group 1 | Nets, overhead cover, HPM | 7–24 s window — passive must already be in place |
| Saturation salvo | Cheap interceptors + hardening | Never trade expensive for cheap |
| Swarm | **HPM** | Only area effector; lasers engage serially |
| Pre-positioned close-launch | Overhead cover + human terrain | No warning, no engagement window |
| Contraband delivery | RF detection to locate the operator | Interdict the person, not the platform |

### 8.8 Infrastructure improvement measures

#### 8.8.1 JIATF 401 "Harden, Obscure, Perimeter" (HOP)

The governing framework from the 401 *Guide for Physical Protection of Critical
Infrastructure* (30 Jan 2026). Audience: installation commanders, base defenders, local
law enforcement, interagency partners, security forces. Emphasis throughout is on
**passive, low-cost measures that do not require procuring exquisite technology.**

| Element | Definition | Measures named |
|---|---|---|
| **Harden** | Create physical obstacles to sUAS flight | Concrete walls · hardened roofs · overhead netting · tensioned cables · **closing retractable roofs and covering roof openings where feasible** · wire, mesh, or fishing line · structural shielding |
| **Obscure** | Reduce what a drone or operator can see and identify | Temporary walls · visual clutter to break up overhead views · decoys · camouflage netting · **diversions to draw attack away from a more important target** |
| **Perimeter** | Extend security beyond the traditional fenceline | Increased patrols · checkpoints · layered zones · staff training to spot suspicious behavior · **revision of crowd and workforce flow design** |

**The perimeter mechanism — four effects from one measure.** Extending the perimeter is
not only about earlier detection. It is expected to **strain UAS batteries, degrade
control links, expose operators, and create a larger safety buffer.** The "expose
operators" effect is the link to interdiction.

**Framing:** *"Traditional access control models are insufficient against sUAS that
operate from stand-off distances."* This matches the conclusion reached independently
from the Spiderweb analysis in §2.

> **Policy context.** This guidance represents a reversal of a prior institutional
> position — US military officials had for years pushed back on the utility and
> cost-effectiveness of physical hardening. Useful if hardening is challenged on cost
> grounds in the room.

#### 8.8.2 Supporting measures

**Overhead cover / hardening**
- USACE Modular Protective System–Overhead Cover, modified for drone threats — lightweight, rapidly deployable panels rated against small loitering-munition payloads
- Overhead cover for all above-ground elements, blast entrances, internal segmentation to contain shrapnel
- Russia began hasty blast-resistant hardened aircraft shelter construction by July 2025, directly following Spiderweb

**Netting / entanglement**
- Ukraine: ~500 miles of anti-drone net tunnels installed, targeting 2,500 miles by end 2026; ~$37M allocated
- Applied to roads, refineries, and 40+ apartment buildings in Shebekino
- **Effectiveness is mixed and unproven.** A Ukrainian commander reports it effective "but Russian pilots are still finding ways to attack." Russian testing showed entanglement worked at a range, but "in real conditions the nets have yet to prove their effectiveness." Netting at a Russian oil facility **failed** to stop a strike. Treat as partial mitigation against cheap analog-video FPVs, not a solution.
- Cheap in materials, expensive in labor

**Infrastructure-specific**
- Composite panels for ballistic protection
- Underground routing of utilities
- Hardening of key nodes plus redundancy in control systems
- "Hardening, obscuration, and extended perimeters work best when layered together"

**Organizational**
- UAS incident response procedures; law enforcement coordination
- **Restriction of publicly available information about equipment locations** — direct doctrinal support for the FIND axis
- Many measures "do not require specialized counter-UAS systems... practical, non-technical actions at modest cost"

### 8.9 Ukrainian command post lessons (CALL)

From *Battalion Command and Observation Posts: Practical Advice Based on War Experiences*.
Russia locates command posts through **four vectors**, all of which are siting decisions:

1. Scanning for radio emissions
2. Analyzing satellite imagery
3. Drone-spotting **clusters of vehicles**
4. Finding **clusters of cell phone signals**

Mitigations:
- **Underground facilities** give the most protection from both detection and indirect fire; basements mask electromagnetic emissions
- **Avoid HF** — strong emissions, easily recognised signature; if unavoidable, lowest power plus terrain masking
- **Decoy emitters** placed away from the real site in a believable configuration
- **Minimize personnel** — "bringing more people almost exponentially increases a position's signature"

### 8.10 Negative case studies

**COP Keating** (3 Oct 2009) — sited deep in a bowl in Nuristan, surrounded by high
ground, limited overwatch from OP Fritsche.

**COP Kahler / Wanat** (2008) — large open field near the village, ringed by prominent
ridges approaching 10,000 ft on all four cardinal approaches.

Operative lesson: *"If you don't have the dominant terrain, you have to have cover or
some way to ensure that the enemy can't use it against you."*

This produces the framework's **terrain denial** concept — you either hold the overwatch,
deny it, or accept being overmatched. There is no fourth option, and "accept" is a veto.

**Correction from wider research (see Pattern D):** elevation is the wrong variable.
**OP Bari Alai** (Kunar, 1 May 2009) was a fortified *mountaintop* OP and was overrun anyway —
attackers pinned the defenders with machine-gun fire while others scaled the slopes. The summit
gave observation; the slopes gave covered approaches. The CSI Wanat study has the correct
formulation: "surrounded by mountains and low ground, **resulting in extensive dead space**."
**Score dead space, not height.**

### 8.11 Recurring failure patterns across conflicts

Synthesized across individually-sourced cases. **No published cross-conflict synthesis of outpost
siting failure appears to exist** — searches for one returned nothing — so this is original
analysis, not a literature summary. Present it as such.

| # | Pattern | Cases | Strength |
|---|---|---|---|
| **A** | **"Temporary" defeats "defensible."** Intent to occupy briefly justifies not hardening; the occupation outlasts the intent. | Isandlwana 1879 · Wanat 2008 · Camp Bastion 2012 | **Strong — spans 3 centuries** |
| **B** | **Forward position administratively reclassified as rear.** | FSB Mary Ann 1971 · Nahal Oz 2023 | **Strong — near-identical findings 52 years apart** |
| **C** | **Sited for presence/population against defensibility, without adjusting the force.** | COP Ranch House · Wanat · Keating | Strong |
| **D** | **High ground necessary but not sufficient.** Dead space, not elevation, is operative. | OP Bari Alai · FSB Ripcord | Moderate |
| **E** | **Mutual support asserted, not verified.** A property of the manned configuration, not the plan. | Bar-Lev Line · Camp Bastion · Keating | Moderate-strong |
| **F** | **Critical dependencies sited outside the defensible perimeter.** | Khe Sanh (water) · Wanat (fuel, water) · COP Zerok (single approach road) · Israeli security zone (convoy resupply) | Moderate |
| **G** | **Outpost creep.** A small position accretes logistics, then protection for the logistics, becoming a target it was not when established. | Israeli security zone in Lebanon | Moderate |
| **H** | **Predecessor incident treated as an anomaly rather than a class** — and the transition is the danger window. | Ranch House (Aug 2007) → Wanat (Jul 2008), same brigade, same valley system | Moderate |

**Pattern A, the 1879 illustration.** Chelmsford intended Isandlwana as a temporary camp, therefore
**ordered Pulleine not to entrench** — contrary to standing orders — and refused a request to laager
the wagons, reportedly saying "It would take a week to make." Wood's troops at Khambula, who did
fortify with wagon walls and trenches, survived. The identical logic produced uncleared fields of
fire at Wanat (engineer equipment without fuel) and poppy growing to the fence line at Camp Bastion.

**Pattern B, the two texts side by side.**
- FSB Mary Ann: *"The soldiers atop the hill had come to regard their outpost as something of a rear
  echelon area rather than what it actually was — the division's most forward firebase."* No
  coordinated defense plan existed because no such plans existed. MACV IG traced fault to division
  command level.
- Nahal Oz: *"supposed to be a forward base but was treated as a rear outpost amid financial
  constraints."* Not drilled for attack; defensive positions facing Shuja'iyya empty; watchtowers
  empty with machine guns locked in storage; one sentry for the entire base. Overrun in under two
  hours. IDF probe: "the biggest failure" of 7 October.

**Pattern E, best documented.** Camp Bastion, 14/15 Sept 2012 — two independent official
investigations (UK Defence Committee and USCENTCOM 15-6). Tower selection *was* based on "the
external terrain and interlocking fields of fire and observation," and manning was rotated
deliberately to avoid setting a pattern — but only ~50% of towers were manned, and **the tower
closest to the breach point, Tower 16, was unmanned.** The Defence Committee found this
"contributed directly to the failure to detect the insurgents at an early stage."

### 8.12 Comparative standoff and siting standards

Useful for framing, but note the critical limitation below.

| Regime | Figure | Basis |
|---|---|---|
| **State / SECCA** (diplomatic, overseas) | **100 ft** from property perimeter, or engineering-equivalent blast performance | 22 U.S.C. § 4865 |
| **DOJ 1995** (federal civilian, post-Oklahoma City) | **100 ft** for new federal field offices | DOJ Vulnerability Assessment |
| **DoD UFC 4-010-01** | **45 m / 25 m** billeting & primary gathering; **25 m / 10 m** inhabited buildings; **10 m (33 ft)** absolute floor | Graduated by level of protection and construction type |
| **DHS / ISC** | **No public number** | Criteria in FOUO Design-Basis Threat appendix |
| **Israel** (shelter access route) | **50 m** default · **70 m** forward settlement · **100–150 m** rear settlement with approval | Civil Defense Regulations 1990 |
| **FEMA** (community safe room access) | **5 min walk**, or **0.25 mi walking**, or **0.5 mi driving** | FEMA P-361 |

> **⚠️ These are ground-threat and blast numbers. None of them are drone-derived.**
>
> UFC standoff rests on an explicit premise: Explosive Weight I is **vehicle-delivered** and there
> is "high confidence it would be detected during a vehicle search." **A drone flies over the vehicle
> search.** 45 m of setback that defeats a car bomb does nothing against a Group 1 quadcopter. Do not
> transfer these figures to the UAS case.

**Two important negatives from the research:**

- **UFC 4-010-01 does not address UAS, drone, or top-attack threats.** Change 3 (24 May 2024)
  addressed progressive-collapse criteria and relocatable-building thresholds. C-UAS is handled
  entirely in the operational/policy lane, not the facility-criteria lane. The gap is real.
- **Israeli building code has not been amended for drones either.** The 2025 change (Amendment 163,
  mamad 9→12 m²) concerns habitability during prolonged sheltering, not attack geometry. Israel's
  drone response has been detection, interception, and alerting — not construction.

**Statutory support for our central claim.** The **Secure Embassy Construction and Counterterrorism
Act of 2022** (S. 4320, in P.L. 117-263) contains a Sense of Congress that setback and co-location
requirements, even with waivers, *"no longer provide the security such requirements used to provide
because of advancement in technologies, such as **remote controlled drones, that can evade walls and
other such static barriers**."* It directs State toward performance-based standards and to keep
setback "as limited as possible." **If the premise that static standoff is obsolete against drones
is challenged, this is the citation.**

### 8.13 Israeli protective construction — transferable specifics

**The floor question, resolved.** HFC guidance for buildings *without* a protected space:

> In a building of **more than three floors**, go to the internal stairwell and position yourself
> where there are **at least two floors above you** — on the stairs, not the landing. All stairwell
> levels are protected **except the ground floor and the two uppermost floors**. Choose a stairwell
> with **no windows and no external walls**; position in its middle.

This resolves the framework's floor paradox (§5) by **demanding both** overhead mass and absence of
apertures, rather than trading one against the other — the stairwell core being the only location in
a non-mamad building where both are available.

**Warning time drives siting distance, and both are revised as threat geography changes.**
Representative HFC warning times: Sderot 15 s · Ashkelon 30 s · Haifa/Tiberias 60 s · Tel Aviv 90 s ·
Eilat ~3 min. When the IDF pushed Hezbollah back from the border, HFC **lengthened** warning times
across the north (Nahariya 15→30 s; Tel Aviv 90 s→2.5 min). Direct precedent for the re-scoring
cadence in §7.

**The probabilistic-defense limit — and why it breaks for drones.** A mamad is **not designed to
survive a direct hit**; it is designed against near-miss blast, fragmentation, and building debris.
The doctrine rests on the improbability of any specific protected space being hit.

> **That is a statistical argument, not an engineering one. It holds against inaccurate area threats
> and fails against a precise threat that can choose its aimpoint.** Much borrowed rocket-shelter
> logic does not survive the transition to drones. Flag this wherever shelter precedent is cited.

**Zero-warning contradiction, unresolved in Israeli code.** The 50–150 m access-route caps assume a
siren grants 15–90 s to reach shelter. Drones have repeatedly delivered **no warning at all** — a
strike 70 km from the Lebanese border with no sirens; the September 2025 Eilat drone that evaded
interception and injured 22. **If warning is zero, distance-to-shelter is irrelevant and only
in-dwelling protection counts.** No Israeli source resolves this in code terms. This independently
corroborates the engagement math in §8.3.

**Drone alert doctrine does exist and differs from rocket doctrine.** HFC maintains a separate alert
category for hostile aerial vehicle intrusion: **do not exit until explicitly instructed** (vs. the
10-minute rule for rockets); the aircraft **may change course and traverse multiple areas**; **you
may not hear an explosion** — absence of a detonation does not mean the threat has passed.

**Threat-model failure worth remembering.** Mamad doors were deliberately built **not to lock from
the inside**, so rescuers could reach incapacitated occupants. On 7 October 2023 attackers exploited
this — civilians were shot through doors while physically holding the handles shut. The rule has
since reversed. **A design assumption embedded a threat model that turned out to be wrong.** Audit
our own assumptions the same way.

**Implementation gap — calibration for any recommendation this framework makes.** Israeli State
Comptroller, January 2026: **~3.2 million residents (33.6%) lack standard protection**; 14% of
schools have none; 56% of hospital beds and 41% of operating rooms are unprotected. A mature,
legally mandated, funded shelter regime is still a third short.

### 8.14 Continuity and redundancy — the FCD 1 principle

**Federal Continuity Directive 1 states no numeric separation distance.** The criteria are:
- Locations **not affected by the same catastrophic event** driving operations from the primary site
- Power, telecommunications, and internet **from grids separate from those serving the primary facility**
- Distinction between **alternate sites** (relocate the staff) and **devolution sites** (geographically
  separated, *separate staff*, assume the essential functions)

**Hazard independence and infrastructure independence, not mileage.** This is a better formulation
than a distance and should govern the SUSTAIN axis. Do not assign a mileage figure to continuity
siting — none exists in the directive.

### 8.15 Survivability vs. effectiveness — the documented cost

The axis doctrine names but does not measure. Now evidenced:

- **GAO-10-767:** State closed public diplomacy facilities and moved others onto secure compounds.
  *"As a result, the number of visitors to these facilities declined and face-to-face interaction
  with foreign publics became more difficult."*
- **GAO-08-162:** at **all 11 posts GAO visited**, site conditions prevented full adherence to
  security standards. Non-compliance is routine, not exceptional.
- **OBO conceding the critique:** the 10-acre site requirement "required siting the embassy too far
  from urban centers where foreign government offices and other embassies are located."
- **Benghazi ARB:** *"the total elimination of risk is a non-starter for U.S. diplomacy."*
- **Best Practices Panel:** asked about the Department's risk management process, ambassadors and
  officers overseas each said **"there is none, and they make it up."**

That last finding is the argument for having a documented framework at all.

---

## 9. Open items and confidence

### Not verified — do not brief as settled

- **Neither JIATF 401 publication has been read directly.** All 401 content here — the
  Four Ps, Five Ds, and the HOP framework in §8.8.1 — derives from secondary reporting.
  This environment's egress policy blocks `media.defense.gov`, `armypubs.army.mil`, and
  related hosts. The HOP structure and the measures listed under it are corroborated
  across several independent outlets and are high confidence; **what remains unseen is
  the guide's internal structure, any specific distances or numeric thresholds, and any
  assessment checklist or scorecard it may contain.** If the source differs, defer to it.
- **ATP 3-01.81 has not been read directly** — same cause. §8.9 and passive-defense
  content is from secondary summary.
- Interceptor cost and success-rate figures (§8.6) are largely **vendor or manufacturer
  claims**. Treat ratios as directional.
- Kill-chain latency of 15–40 s (§8.3) is vendor-adjacent and probably optimistic.
- FPV attack-run speeds are poorly documented publicly. Max-speed figures were used, so
  those rows are conservative-pessimistic.
- One source claimed 60,000 border drone flights in a six-month window versus CBP's
  34,682 for all FY2025. The CBP figure is used; the larger is unverified.
- Legal citations in §3 should be confirmed against current statute and the 6 July 2026
  implementing rule before briefing.

- **§8.11 recurring patterns are original synthesis**, not a literature finding. Searches for a
  published cross-conflict synthesis of siting failure returned nothing. Each underlying case is
  individually sourced; the pattern abstraction is ours. Present it that way.
- **UFC Appendix C Tables C-1 to C-6 cell values were not obtained.** The tables exist at pp. 61–64
  of the 2018 Change 3 edition. The PDF is public and free at wbdg.org — retrievable on an
  unrestricted network. Do not fill these in from memory.
- **UFC explosive weights (kg/lb TNT) are genuinely unobtainable** — FOUO and FOIA-exempt by design,
  requiring a justified request to the USACE Protective Design Center. Any web source claiming to
  state them should be treated as suspect.
- **Authoritative mamad wall-thickness table not obtained.** It is a *table*, not a number — varying
  by protected-space type, count of exposed faces, and window type — in HFC's Architectural Design
  Guidance Binder (Sept 2024), Appendix B. Nearly every single-figure thickness claim online is
  contractor marketing conflating shelter specs with mamad specs. The shelter figures quoted in
  §8.13 are traceable to the 1990 regulations and are reliable; mamad thicknesses are not.
- **No public HAS separation distance could be derived.** The design threat is confirmed (direct hit
  by 500 lb, near-miss by 1,000 lb+, 460 mm concrete); the spacing rule is not public. Do not assert
  a figure.
- **No doctrinal Vietnam firebase spacing standard exists.** Spacing was a derived consequence of the
  105 mm range fan (~11,000 m radius, ~22 km coverage circle) and desired overlap — not a prescribed
  distance. Do not assert one.
- **Bar-Lev Line strongpoint spacing figures conflict** across sources (7 miles / 5–10 km / <5 km /
  5–15 km / <900 m at crossing points). Cite only the qualitative finding — strongpoints "generally
  not in view of one another and could not offer mutual support" — and the ~16-of-30 manned figure.
- "100 ft = Inman standards" is the **conventional but legally imprecise** attribution. CRS states the
  Inman Report specifically did *not* recommend a 100-foot setback or 9-foot walls. **Cite 22 U.S.C.
  § 4865.**

### Not yet done

- **Back-test against Keating and Wanat.** Run both frameworks against the two known
  failures. If v3 does not loudly reject both, the veto conditions are wrong. Cheap test,
  high diagnostic value. Note §8.11 has already forced one veto correction (dead space, not
  elevation), so the test is likely to find more.
- Interdiction profile (§2) is sketched, not built out.
- No worked example or filled-in scorecard yet.

### Priority follow-up reads

1. **JMS 2021, "Siting military base camps through an MCDA framework"** — surveyed US Army officers
   with base camp experience; derived **10 criteria with default weights**, explicitly caveated that
   they must be tailored via scenario-specific weights and value functions. This is our approach,
   arrived at independently, and the single most on-target document found. Open access.
2. **ATP 3-37.10 / MCRP 3-40D.13, *Base Camps*, Table B-2** — "Site selection considerations in
   relation to mission variables (METT-TC)." The doctrinal checklist. Title confirmed, contents not.
3. **UFC 4-010-01 (2018 c3), Appendix C** — the standoff tables.
4. **Corson & Jasperro, "An All-Hazards Approach to US Military Base Camp Site Selection,"**
   *The Geographical Bulletin* 48(2) — open access. Argues all-hazards should be integral to siting
   doctrine rather than tactical/logistical criteria dominating. Kosovo case study.
5. **UFC 4-020-01** — the risk-assessment companion, with worksheet tools already demonstrated as
   adaptable to non-terrorism hazards.
6. **JIATF 401 CIP Guide** — for numeric thresholds and any assessment checklist (see above).

---

## 10. Sources

**Doctrine and official**
- [ATP 3-01.81 Counter-UAS (FAS mirror)](https://irp.fas.org/doddir/army/atp3-01-81.pdf)
- [JIATF-401 Guide for Physical Protection of Critical Infrastructure](https://media.defense.gov/2026/Jan/30/2003868750/-1/-1/0/JIATF-401-GUIDE-FOR-PHYSICAL-PROTECTION-OF-CRITICAL-INFRASTRUCTURE.PDF)
- [Army: Lessons Learned from Ukrainian TDF — CP Survivability](https://www.army.mil/article/273510/lessons_learned_from_the_ukrainian_territorial_defense_forces_command_post_survivability)
- [Line of Departure: Developing Emissions Control SOP](https://www.lineofdeparture.army.mil/Portals/144/PDF/Journals/Armor/Spring-2025/McGovern.pdf)
- [Military Review: Convergence and Emission Control](https://www.armyupress.army.mil/Portals/7/military-review/Archives/English/Nov-Dec-23/Tetreau/Convergence-and-Emission-Control-UA.pdf)
- [CSI: Wanat — Combat Action in Afghanistan, 2008](https://www.armyupress.army.mil/portals/7/combat-studies-institute/csi-books/wanat.pdf)

**Authority**
- [10 USC 130i](https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-prelim-title10-section130i&num=0&edition=prelim)
- [CRS: DoD Counter-UAS — Background and Issues for Congress (R48477)](https://www.congress.gov/crs-product/R48477)
- [CRS: Law Enforcement and the Evolving C-UAS Landscape (IN12661)](https://www.congress.gov/crs-product/IN12661)
- [Federal Register: C-UAS Authority for SLTT LE and Correctional Agencies (6 Jul 2026)](https://www.federalregister.gov/documents/2026/07/06/2026-13609/counter-uas-authority-for-state-local-tribal-and-territorial-law-enforcement-and-correctional)
- [Lawfare: The Counter-UAS Certification Bottleneck](https://www.lawfaremedia.org/article/the-counter-uas-certification-bottleneck)

**Threat and effectiveness**
- [CSIS Missile Defense Project: Shahed-131 / -136](https://missilethreat.csis.org/missile/shahed-131-and-136/)
- [MDPI: Small fixed-wing UAV RCS investigation](https://www.mdpi.com/2504-446X/7/1/39)
- [Beechat: How modern drones overcome jamming](https://beechat.network/2026/01/05/how-modern-drones-overcome-jamming-fibre-optics-ai-autonomy-and-frequency-hopping/)
- [TWZ: Cheap interceptor drones proven in Ukraine](https://www.twz.com/land/cheap-interceptor-drones-proven-in-ukraine-protected-u-s-troops-against-iranian-shaheds)
- [CSIS: Calculating the cost-effectiveness of Russia's drone strikes](https://www.csis.org/analysis/calculating-cost-effectiveness-russias-drone-strikes)
- [Corvus: C-UAS detect-track-identify-defeat architecture](https://corvusintell.com/blog/c2-systems/counter-uas-c2-software/)
- [Wikipedia: Operation Spiderweb](https://en.wikipedia.org/wiki/Operation_Spiderweb)

**Hardening and passive defense**
- [TWZ: Hardened structures, nets front and center in new Pentagon guidance](https://www.twz.com/news-features/hardened-structures-nets-for-drone-defense-front-and-center-in-new-pentagon-guidance)
- [TWZ: Army modular shelter kit improvements](https://www.twz.com/news-features/growing-drone-threats-lead-to-army-modular-shelter-kit-improvements)
- [MWI: Survival Skills — Why the Army Needs to Relearn Passive Defense](https://mwi.westpoint.edu/survival-skills-why-the-army-needs-to-relearn-passive-defense/)
- [ICDS: Russia's War in Ukraine — Fortification for Drone Warfare](https://icds.ee/en/russias-war-in-ukraine-fortification-for-drone-warfare/)
- [Forbes: FPVs are changing the rules of urban warfare](https://www.forbes.com/sites/davidhambling/2026/05/05/drone-hide-and-seek-fpvs-are-changing-the-rules-of-urban-warfare/)

**Homeland incident data**
- [FPRI: Small Drones, Big Problems — Managing the Unmanned Threat to the Homeland](https://www.fpri.org/article/2025/09/small-drones-big-problems-managing-the-unmanned-threat-to-the-homeland/)
- [TWZ: NORAD commander on Langley AFB incursions](https://www.twz.com/air/heres-what-norads-commander-just-told-us-about-the-langley-afb-drone-incursions)
- [Unmanned Airspace: PA substation drone attack](https://www.unmannedairspace.info/uncategorized/attempted-attack-on-a-power-substation-in-pennsylvania-attributed-to-a-malicious-drone/)
