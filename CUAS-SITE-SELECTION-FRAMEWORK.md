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
| **REACH** | Terrain overmatch — who holds, or could hold, dominating ground · vehicle-accessible launch points inside effective range · dead space and infiltration routes · perimeter standoff tiered by threat class |
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
| Dominating terrain held by no one and deniable by no one | The Wanat / COP Keating failure mode |
| No egress — single route in and out | Choke point that no concealment fixes |
| No interior refuge without an exterior wall | No survivable position exists |
| Sustainment failure inside tolerance window | MLCOA harm is utility loss, not blast |
| Unacceptable on a **non-drone** hazard (flood, fire, casevac time, civil disorder) | Guards against over-fitting to one threat |

**3. Re-score on a cadence.** FPV range moved from 5–10 km to 25 km in roughly two
years; fiber-optic control defeated RF jamming outright. Every score has a shelf life.
Annual minimum, or on any observed capability shift.

**4. Define abandonment triggers at selection time**, not later. What observation makes
this site non-viable?

**5. "No acceptable site" is a valid output.** Relocation must be an allowed answer,
not a failure state.

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

---

## 9. Open items and confidence

### Not verified — do not brief as settled

- **Neither JIATF 401 publication has been read directly.** All 401 content here derives
  from secondary reporting. This environment's egress policy blocks `media.defense.gov`,
  `armypubs.army.mil`, and related hosts. If the 401 *Guide for Physical Protection of
  Critical Infrastructure* (media.defense.gov, Jan 2026) differs from §8.8, **defer to
  the source**.
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

### Not yet done

- **Back-test against Keating and Wanat.** Run both frameworks against the two known
  failures. If v3 does not loudly reject both, the veto conditions are wrong. Cheap test,
  high diagnostic value.
- Interdiction profile (§2) is sketched, not built out.
- No worked example or filled-in scorecard yet.

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
