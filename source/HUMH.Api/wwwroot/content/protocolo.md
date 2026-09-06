# HUMH: Reality Structured By The Observer
# Experimental Protocol - Complete Version v1.6

**Author:** Luciano Vianna  
**ORCID:** https://orcid.org/0009-0000-5591-3577  
**Email:** luciano.vianna@outlook.com  
**OSF Project:** https://osf.io/s79zj/

**Version:** 1.6  
**Date:** July 26, 2026  
**Status:** 🔓 OSF registration OPEN — freeze this version BEFORE data collection

**Design:** 2 Groups (FV vs SF) | N=70 | 49 Trials | Visual Feedback Only

**Status:** ✅ **v1.6 - Ready for OSF Pre-registration**

**Experiment:** `experimento.html` v1.2.1 (deployed at Azure)  
**Analysis:** `dados.html` (JavaScript interactive dashboard)  
**Platform:** Prolific Academic

---


---

## VERSION HISTORY

### v1.5 FINAL (November 26, 2025)
**Major Changes:**
- ✅ **Hypotheses reorganized:** Core (H1, H2) + Proxy (H3) + Derived (H4, H5, H6) + Exploratory (E1, E2)
- ✅ **H2 redefined:** Observational Resistance (β > 0) - universal resource limitation
- ✅ **H3 redefined:** Symbolic Compression (proxy for perceptual loop)
- ✅ **Added H4:** EH Structural Symmetry
- ✅ **Added H5:** Perceptual (not Motor) Compression
- ✅ **Added H6:** β as Individual Parameter
- ✅ **Renamed H2a/H2b → E1/E2:** Feedback and Accuracy (Exploratory)
- ✅ **RT exclusion:** Conditional by accuracy (RT < 300ms excluded only if incorrect)

### v1.4 FINAL (November 2025)
- Visual feedback only (no auditory)
- N=70 participants
- 49 trials per participant
- Prolific recruitment

---

## 1. EXECUTIVE SUMMARY

### Experimental Design

**Type:** Between-subjects (2 groups) + Within-subjects (EH levels)

**Groups:**
```
├─ FV (Full Feedback): N=35
│  └─ Visual feedback (✓ green / ✗ red, 300ms)
│
└─ SF (Sans Feedback): N=35
   └─ Pure baseline (HUMH without external interference)
```

**Structure:**
- **49 trials** per participant (5-7 minutes)
- **P_CORE:** 3/11, 5/11, 6/11, 8/11 (50/50 color balance)
- **Platform:** Prolific Academic
- **Recruitment:** English-fluent, desktop only

**Statistical Power (current hypothesis taxonomy):**
- H1 (EH→RT, paired contrast): **0.92** ✅
- H2 (β > 0, lag regression ΔRT = α + β·lag): **⚠️ PENDING recalculation** — prior power was computed for the old FV-vs-SF contrast, not for the slope test with 4 pairs per lag per participant. Must be recomputed (simulation-based) before N is finalized.
- H3 (α < 0, repetition benefit): **0.98** ✅ (computed for the repetition contrast; conservative proxy for α)
- E1/E2 (FV vs SF, exploratory): **0.69** — acceptable for exploratory status

**Total Cost:** £126 (70 participants × £1.80)

---

## 2. RESEARCH QUESTION

**Primary Question:**  
Does the HUMH framework accurately predict perceptual convergence dynamics, including:
1. RT increase with Harmonic Entropy (EH)
2. Feedback acceleration of learning
3. Symbolic compression under finite maintenance resources (β > 0)

**Secondary Question (Exploratory):**  
Does HUMH make unique structural predictions that distinguish it from alternative theories (DDM, Bayesian)?

---

## 3. HYPOTHESES

### 3.1 Confirmatory Hypotheses - Core (Direct Tests of Central Concepts)

These hypotheses test the most central theoretical concepts of HUMH through direct empirical observation.

---

#### **H1: Harmonic Entropy → Observational Cost (RT)**

**Note:** Observational cost is measured as Reaction Time (RT) in human observers. This is a domain-specific manifestation of the universal HUMH principle that convergence requires resource expenditure proportional to initial entropy. In human cognitive tasks, observational cost manifests as RT due to the perceptual loop cycles necessary for reducing uncertainty to actionable levels.

**Prediction:**
```
RT(EH_High) > RT(EH_Low)
Cohen's d ≥ 0.40
p < 0.05 (one-tailed)
```

**Operationalization:**
- **EH_High** = 0.9091 (p = 5/11 or 6/11)
- **EH_Low** = 0.5455 (p = 3/11 or 8/11)

**HUMH Mechanism:**
High EH → initial state p₀ near repulsor (0.5) → slow convergence → more observational loop cycles → increased observational cost (manifested as RT)

**Tested in:** SF group (no feedback = pure HUMH baseline)

**Statistical Test:**
- **Method:** Independent t-test (Welch's, unequal variances)
- **Groups:** RT(EH_High) vs RT(EH_Low) in SF group only
- **Direction:** One-tailed (RT_High > RT_Low)
- **Effect size:** Cohen's d
- **Implementation:** See `dados.html`

**Validation Criteria:**
- p < 0.05 (one-tailed)
- Cohen's d ≥ 0.40

**Exploratory:** Does H1 also appear in FV group? If yes, EH is robust even with external feedback.

---

#### **H2: Observational Resistance (β > 0)**

**Objective:** Test whether β > 0 (observational resistance parameter), indicating that maintaining observational states requires continuous resource expenditure in dissipative environments.

**HUMH Principle:**  
β represents a **universal principle** of observational systems: maintaining observational order requires finite resources. When β > 0, observational states degrade over time unless actively maintained.

**Cognitive Manifestation:**  
In human observers, β > 0 manifests through:
- Working memory capacity limitations
- Sustained attention costs
- Perceptual trace degradation

**Statistical Model:**
```
ΔRT = α + β × lag

Where:
- ΔRT = RT(2nd) - RT(1st)  [negative = compression/facilitation]
- lag = trials between pair presentations (1, 2, or 3)
- α = baseline compression effect (should be < 0)
- β = observational resistance rate (should be > 0)
```

**Implementation:**
- **12 identical pairs** per participant (24 paired trials)
- **Variable lag (stratified):** each p_level receives lags {1, 2, 3} — exactly one pair per lag per level (4 pairs per lag overall). Pair-block order randomized per participant.
- Same p_level + same spatial_seed = visually IDENTICAL stimuli
- Total: 12 pairs × 70 participants = 840 observations

**HUMH Mechanism:**
- Compression benefit exists (α < 0)
- Observational states require continuous maintenance → benefit degrades with lag (β > 0)
- Human systems: β > 0 (finite attention/working memory resources)
- Computational systems: β ≈ 0 (effectively unlimited RAM/cache maintenance)

**Why β > 0 is Universal (Not Just Cognitive):**
β reflects finite maintenance resources in ANY observational system:
- **Cognitive:** Limited attention, working memory decay
- **Neural:** Metabolic cost of maintaining synaptic states
- **Computational:** Cache invalidation, RAM refresh cycles
- **Social:** Communication bandwidth, coordination costs
- **Physical:** Energy required to maintain measurement apparatus

**Statistical Test:**
- **Method:** Linear regression (ordinary least squares)
- **Model:** ΔRT = α + β × lag
- **Data:** 12 identical pairs per participant (24 paired trials); stratified lags {1,2,3}, 4 pairs per lag
- **Tests:** 
  - H2: One-tailed t-test on β (tests β > 0)
  - H3: One-tailed t-test on α (tests α < 0)
- **Implementation:** See `dados.html`

**Validation Criteria (H2):**
- β > 0, p < 0.05 (one-tailed)
- R² > 0.10 (model explains variance)

---

#### **H3: Symbolic Compression (Proxy for Perceptual Loop)**

**Objective:** Test whether compression exists (α < 0), as indirect evidence for the perceptual loop's state maintenance across trials despite β > 0 degradation.

**Statistical Model:**
```
α < 0 (compression exists)
```

**CRITICAL NOTE:**
> While the perceptual loop is theoretically central to HUMH, this experiment
> tests it **indirectly** through compression effects between trials. The loop
> operates at millisecond timescales **within** individual trials (convergence
> from high EH to low EH via iterative cycles). Our behavioral paradigm does
> not observe this within-trial dynamics.
> 
> Instead, we measure facilitation when the same stimulus is presented again
> after several intervening trials. This tests whether compressed representations persist despite β > 0
> (second exposure faster than first), but not the iterative convergence
> mechanism directly.
> 
> Direct observation of the loop would require continuous measures during
> trials (e.g., eye-tracking to observe fixation patterns, EEG to observe
> neural convergence), which are beyond the scope of this behavioral study.

**Statistical Test:**
- **Method:** Uses same linear regression as H2: ΔRT = α + β × lag
- **Test:** One-tailed t-test on α (intercept)
- **Prediction:** α < 0 (baseline compression exists)
- **Implementation:** See `dados.html`

**Validation Criteria:**
- α < 0, p < 0.05 (one-tailed)

**Why this is a proxy:**
- Tests: Compression persistence (α < 0) under β > 0 degradation across trials
- Doesn't test: Iterative convergence within trials
- Limitation: Indirect measure of loop mechanism

---

### 3.3 Confirmatory Hypotheses - Derived (Structural Implications)

These hypotheses test necessary implications of the core concepts. They are "derived" because they follow logically from core principles.

---

#### **H4: EH Structural Symmetry**

**Prediction:**
```
|RT(p=3/11) - RT(p=8/11)| / mean < 0.10
t-test non-significant (p > 0.10)
```

**Rationale:**
- HUMH predicts **exact symmetry** because EH(0.27) = EH(0.73) mathematically
- DDM may show asymmetry due to response bias (e.g., preference for left/right)
- This tests whether RT structure truly reflects EH, not just "harder stimuli are slower"

**Statistical Test:**
- **Method:** Independent t-test (Welch's, unequal variances)
- **Groups:** RT(EH_High) vs RT(EH_Low) in SF group only
- **Direction:** One-tailed (RT_High > RT_Low)
- **Effect size:** Cohen's d
- **Implementation:** See `dados.html`

**Validation Criteria:**
- Relative asymmetry < 10%
- t-test non-significant (p > 0.10) supports symmetry

**Why HUMH-specific:**
- DDM: Drift rate symmetric, but starting point bias can create asymmetry
- HUMH: EH symmetry → RT symmetry (structural prediction)

---

#### **H5: Perceptual Compression (not Motor)**

**Prediction:**
```
ΔRT < 0 even when response differs between pair presentations
Both groups (same response AND different response) show p < 0.05
```

**Rationale:**
- HUMH compresses **perceptual structure**, not motor response
- Classical priming depends on response repetition (motor facilitation)
- This tests whether compression is truly perceptual vs motor

**Validation criteria:**
- ΔRT < 0 for both groups (same response AND different response)
- Both p < 0.05 (one-tailed)

**Why HUMH-specific:**
- Motor priming: Only works if response repeats
- HUMH: Works even if response changes (perceptual loop compression)

---

#### **H6: β as Individual Parameter**

**Prediction:**
```
Within-participant CV < 0.30
Between-participant variance significant (F-test p < 0.05)
```

**Rationale:**
- β is stable individual parameter (observational resistance)
- Should be consistent within person, vary between people
- DDM has no equivalent concept

**Validation criteria:**
- Mean CV < 30% (within-participant consistency)
- F-test significant (between-participant variance)

**Why HUMH-specific:**
- DDM: No equivalent to β (threshold 'a' serves different function)
- HUMH: β = observational resistance, individual parameter

---

### 3.4 Exploratory Hypotheses (Secondary Mechanisms)

These hypotheses test mechanisms that are NOT central to HUMH's core framework but are of interest.

---

#### **E1: Feedback Accelerates Learning (EXPLORATORY)**

**Prediction:**
```
slope_RT(FV) < slope_RT(SF) < 0
Cohen's d ≥ 0.35
```

**HUMH Mechanism:**
- Feedback provides external information that calibrates prior
- Perceptual loop incorporates feedback as Bayesian update
- Accelerated convergence = fewer cycles needed in later trials

**Why exploratory:**
- Feedback is NOT central to HUMH's individual-level theory
- Theory mentions "loops temporais de feedback" (internal feedback: perception → update)
- External feedback is mentioned only in Pipeline C2C (collective level)
- HUMH does not make strong prediction about external feedback acceleration

**Statistical Test:**
- **Method:** Independent t-test (Welch's, unequal variances)
- **Groups:** RT(EH_High) vs RT(EH_Low) in SF group only
- **Direction:** One-tailed (RT_High > RT_Low)
- **Effect size:** Cohen's d
- **Implementation:** See `dados.html`

**Validation Criteria:**
- slope_FV more negative than slope_SF
- Both slopes negative (learning occurs)
- Cohen's d ≥ 0.35

---

#### **E2: Final Accuracy Difference (EXPLORATORY)**

**Prediction:**
```
Accuracy(FV, trials > 29) > Accuracy(SF, trials > 29)
Difference ≥ 5 percentage points
Cohen's d ≥ 0.30
```

**HUMH Mechanism:** Feedback calibrates perception → improves discrimination in later trials

**Why exploratory:**
- HUMH predicts both groups converge (EH→0), but not necessarily different final accuracy
- External feedback calibration is not central mechanism

**Statistical Test:**
- **Method:** Independent t-test (Welch's, unequal variances)
- **Groups:** RT(EH_High) vs RT(EH_Low) in SF group only
- **Direction:** One-tailed (RT_High > RT_Low)
- **Effect size:** Cohen's d
- **Implementation:** See `dados.html`

**Validation Criteria:**
- p < 0.05 (one-tailed)
- Difference ≥ 5 percentage points
- Cohen's d ≥ 0.30

---

### 3.5 Validation Logic

**HUMH Validation (Hierarchical):**

#### **MINIMAL VALIDATION:**
```
H1 (EH) OR H2 (β) confirmed
```
→ At least 1 core concept empirically validated

---

#### **STRONG VALIDATION:** ⭐ Recommended threshold
```
H1 (EH) AND H2 (β) confirmed
```
→ Both core concepts empirically validated

---

#### **FULL VALIDATION:**
```
STRONG + H3 (proxy) confirmed + ≥2 derived (H4/H5/H6) confirmed
```
→ Core + proxy + structural implications validated

---

#### **COMPREHENSIVE VALIDATION:**
```
All confirmatory hypotheses (H1-H6) confirmed
```
→ Maximum empirical support

---

#### **Exploratory (E1, E2):**
- Do NOT affect HUMH validation status
- Reported as additional findings
- If confirmed: Suggest external feedback modulates convergence
- If not confirmed: Does not invalidate HUMH (not central mechanisms)

---

## SECTION 4.1: EXCLUSION CRITERIA (MODIFIED)

### Participant-Level Exclusion

**Automatic exclusions:**

1. **Failed BOTH attention checks (2/2)**
   - p=1/11 (1 blue, 10 orange) → incorrect response
   - p=10/11 (10 blue, 1 orange) → incorrect response
   - **Rationale:** Failing both indicates systematic inattention
   - Allows 1 human lapse
   - **Literature:** Standard for experiments with 2 checks

2. **Extreme mean RT:**
   - Mean RT < 300ms across all main phase trials → exclude participant
   - Mean RT > 10,000ms across all main phase trials → exclude participant
   - **Rationale:** Systematic fast responding or disengagement

3. **Early abandonment:**
   - Completed < 39/49 trials (< 80%)

4. **Technical issues:**
   - Severe problems reported in post-experiment questionnaire

**Expected losses:**
```
N recruited: 73-75
↓ Attention checks (2-3%) → 71-73
↓ Extreme RT (1%) → 70-71
↓ Abandonment (0-1%) → 70
N_final expected = 70 (35 FV + 35 SF)
```

---

### Trial-Level Exclusion ⭐ CRITICAL CHANGE in v1.5

**PROBLEM:** Excluding ALL trials with RT < 300ms creates bias AGAINST H3 (compression hypothesis).
- Strong compression may legitimately produce RT₂ < 300ms
- Excluding these removes the BEST evidence for compression
- Effect size would be underestimated by ~25-30%

**SOLUTION:** Conditional exclusion based on accuracy.

**Exclusion rules:**

1. **RT < 300ms AND incorrect → EXCLUDE**
   - **Rationale:** Fast incorrect = anticipation (responded before processing stimulus)
   - Not genuine compression

2. **RT < 300ms AND correct → RETAIN**
   - **Rationale:** Fast correct = compression/facilitation (rapid memory-based retrieval)
   - This is EXACTLY what H3 predicts for strong compression
   - **Precedent:** Priming literature ("fast but accurate responses reflect facilitation")

3. **RT > 10,000ms → EXCLUDE**
   - **Rationale:** Task disengagement (regardless of accuracy)

**Justification for reviewers:**
> "We implemented conditional exclusion for fast trials (RT < 300ms) based on 
> accuracy. Fast incorrect responses indicate anticipation (responding before 
> processing the stimulus) and were excluded. However, fast correct responses 
> were retained, as these may reflect strong compression/facilitation from 
> prior exposure - precisely what H3 predicts. Excluding all fast trials would 
> create bias against the compression hypothesis by removing the strongest 
> evidence. This approach is consistent with priming literature, where 'fast 
> but accurate' responses are considered evidence of facilitation."

---

END OF MODIFIED SECTIONS

---

For complete protocol v1.5, these sections replace the corresponding sections in v1.4.
All other sections remain unchanged.


## 4. METHOD

### 4.1 Participants

#### Sample Size

| Parameter | Value |
|-----------|-------|
| **N total** | 70 |
| **Group FV** | 35 |
| **Group SF** | 35 |
| **Recruitment** | Prolific Academic |
| **Compensation** | £1.80 per session (~7-10 min) |
| **Expected exclusion rate** | 3-5% |
| **N to recruit** | 73-75 (buffer) |

**Total Cost:** £126-135 (70-75 participants × £1.80)

---

#### Inclusion Criteria (Prolific)

**Pre-screening filters:**
- Age: 18-65 years
- Approval rate: ≥ 95%
- Number of submissions: ≥ 50
- **Device: Desktop ONLY** (mobile/tablet blocked via Prolific)
- Fluent in English
- Country: UK, US, Canada, Australia, Ireland, New Zealand (native English speakers preferred)

**Rationale:**
- High approval rate ensures reliable participants
- Desktop requirement ensures standardized display (11×11 grid needs stable resolution)
- English fluency for instructions comprehension

---

#### Exclusion Criteria (Pre-Analysis)

**Automatic exclusions:**

1. **Failed BOTH attention checks (2/2)**
   - p=1/11 (1 blue, 10 orange) → incorrect response
   - p=10/11 (10 blue, 1 orange) → incorrect response
   - **Rationale:** Failing both indicates systematic inattention; allows 1 human lapse
   - **Literature:** Standard for experiments with 2 checks (Oppenheimer et al., 2009)

2. **Extreme RT (by trial, main phase):**
   - Mean RT < 300ms (too fast - random responding)
   - Mean RT > 10,000ms (too slow - task disengagement)

3. **Early abandonment:**
   - Completed < 39/49 trials (< 80%)

4. **Technical issues:**
   - Severe problems reported in post-experiment questionnaire

**Expected losses:**
```
N_recruited = 73
↓ Attention checks (1-2%) → 71-72
↓ Extreme RT (1%) → 70-71
↓ Abandonment (0-1%) → 70
N_final expected = 70 (35 FV + 35 SF)
```

**Note:** Requiring failure on BOTH checks (not ≥1) reduces unnecessary exclusions of honest participants who had momentary lapse.

---

### 4.2 Experimental Design

#### Trial Structure

**Total: 49 trials per participant (5-7 minutes)**

```
49 trials:
├─ Phase 1: CALIBRATION (8 trials)
│  ├─ P_EXTRA = [1/11, 2/11, 9/11, 10/11] × 2
│  ├─ Function: Individual RT baseline
│  └─ Feedback: Yes (all groups - visual only for SF, visual+audio for FV)
│
├─ Phase 2: TRAINING (4 trials)
│  ├─ P_EXTRA = [4/11, 5/11, 6/11, 7/11]
│  ├─ Function: Task familiarization
│  └─ Feedback: MATCHING - FV yes (visual+audio), SF no
│
└─ Phase 3: MAIN (37 trials)
   ├─ 24 paired identical trials (H3)
   │  └─ 4 levels × 3 pairs × 2 = 24 trials
   ├─ 11 unique trials (balance + variability)
   └─ 2 attention checks (p=1/11, p=10/11)
```

**Total:** 8 + 4 + 37 = **49 trials**

---

#### Proportion Levels (p)

**P_CORE (main phase):** 4 levels
```
- 3/11 (0.27): 3 blue, 8 orange → EH = 0.5455 (Low)
- 5/11 (0.45): 5 blue, 6 orange → EH = 0.9091 (High)
- 6/11 (0.55): 6 blue, 5 orange → EH = 0.9091 (High)
- 8/11 (0.73): 8 blue, 3 orange → EH = 0.5455 (Low)
```

**Balance:** 50% Orange vs 50% Blue (CRITICAL for symmetry)

**P_EXTRA (calibration/training):**
```
- 2/11, 4/11, 7/11, 9/11
```

**Attention checks:**
```
- 1/11: 1 blue, 10 orange (trivial)
- 10/11: 10 blue, 1 orange (trivial)
```

---

#### Feedback by Group

**Group FV (Full Feedback) - N=35**

**Visual Feedback (300ms):**
- ✓ (green #00AA00, 64px) if correct
- ✗ (red #CC0000, 64px) if incorrect
- Opacity: 0.85 (discrete but visible)
- Position: Center of screen
- Duration: 300ms

**Phases with feedback:**
- Calibration: Yes (visual)
- Training: Yes (visual)
- Main: Yes (visual)

**Rationale:** Visual-only feedback is:
- More consistent across participants (no volume variability)
- Standard in cognitive psychology literature
- Sufficient for learning (Ratcliff & McKoon, 2008)
- Avoids technical issues (Web Audio API compatibility)

---

**Group SF (Sans Feedback) - N=35**

**No feedback in main and training phases**

**Calibration only:**
- Visual feedback only
- Purpose: Allow participants to understand task before removing feedback

**Phases with feedback:**
- Calibration: Yes (visual only)
- Training: No
- Main: No

---

#### Identical Pairs (H3)

**Implementation:**
- **12 pairs** per participant (24 trials total)
- **3 pairs** per p_level (4 levels × 3 = 12 pairs)
- **Variable lag (stratified):** lags {1, 2, 3}, one pair per lag within each p_level; block order randomized per participant
- **Visual identity:** Same p_level + same spatial_seed = deterministic identical grid

**Lag Generation (v1.2.1 implementation):**
- Each p_level's 3 pairs are assigned lags {1, 2, 3} in shuffled order (stratified randomization)
- Pair blocks are shuffled, then interleaved with filler trials so that exactly (lag − 1) fillers separate the two presentations
- Filler pool is sized so no lag is ever truncated (guaranteed by count: 12 gap-fillers needed ≤ 13 available)
- Attention checks are part of the filler pool and therefore distributed across the session

**Example:**
```
Trial 15: p=5/11, seed=42 → pair_id = "pair_0_1_1"
Trial 16: [non-paired filler]
Trial 17: [non-paired filler]  
Trial 18: p=5/11, seed=42 → pair_id = "pair_0_1_2"
   ↑ VISUALLY IDENTICAL, lag = 3
```

**Rationale for variable lag:**
- Working memory span: ~2-3 trials (Cowan, 2001)
- Lag 1-3 tests decay within working memory
- Allows regression ΔRT ~ lag to estimate decay rate β

**Critical:** Lag is recorded in data for each pair

---

### 4.3 Stimuli

**Display (as implemented in experimento.html v1.2.1):**
- Single row of **11 dots** (CSS grid, 11 columns), nA blue + nB orange, nA + nB = 11
- Colors: Blue (#5B9BD5) vs Orange (#FF9F43)
- Dot size: 18px diameter, 4px gap, container max-width 440px
- Background: White
- p_level = nA/11; arrangement deterministic from spatial_seed (ensures pair identity)

**Randomization:**
- Spatial positions: Deterministic from spatial_seed (ensures pair identity)
- Trial order: Shuffled while maintaining pair structure
- Group assignment: Prolific Taskflow (two condition URLs, balanced 35/35); client-side validation with random fallback

---

### 4.4 Procedure

**1. Prolific Recruitment**
- Study posted with pre-screening filters
- Estimated time: 7-10 minutes
- Reward: £1.80 (£15.43/hour rate)
- Study URL: https://humh-deg8f0a6hzhtgyfu.brazilsouth-01.azurewebsites.net/experimento.html

**2. Consent & Instructions**
- Information sheet displayed
- Explicit consent required (checkbox)
- Instructions: "Identify which color (blue or orange) appears MORE frequently"
- Response: LEFT arrow (blue more) or RIGHT arrow (orange more)

**3. Experiment**
- Calibration phase (8 trials, with feedback)
- Training phase (4 trials, FV gets feedback)
- Main phase (37 trials, group-specific feedback)
- Each trial:
  - Fixation cross (500ms)
  - Stimulus (until response)
  - Feedback (300ms for visual, group-dependent)
  - ITI (500ms)

**4. Post-Experiment**
- Brief questionnaire:
  - Any technical issues?
  - Strategy used?
  - Comments?
- Prolific completion code: **HUMH2025**
- Automatic redirect to Prolific

---

### 4.5 Data Collection

**Automatic logging (per trial):**

**Backend:**
- ASP.NET Core + SQLite
- Deployed at Azure
- CORS enabled for Prolific
- Real-time data storage
    
---

## 5. DATA ANALYSIS PLAN

### 5.1 Data Loading and Preparation

**All analyses performed in JavaScript using `dados.html` interactive dashboard**


---

### 5.2 Confirmatory Analyses

**Execute tests exactly as specified in Sections 3.1 (H1, H2a, H2b, H3)**

**All code is in JavaScript and executed in `dados.html`**

**Critical:**
- Use one-tailed tests where directional predictions exist
- Report exact p-values and effect sizes
- No p-hacking or optional stopping
- Pre-registered exclusion criteria only

---

### 5.3 Exploratory Analyses

**Execute tests for H4a, H4b, H4c as specified in Section 3.2**

**Additional exploratory:**
- Individual differences in β (H4c extended)
- Group × EH interaction (H1 extended to FV group)
- Learning curves by participant
- Relationship between RT and accuracy

**Note:** Clearly label all exploratory analyses in publication

---

### 5.4 Visualization

**All visualizations generated using Plotly.js in `dados.html`**


---

## 6. STATISTICAL FUNCTIONS

All statistical analyses are implemented in `dados_v1.5_NOMENCLATURA.html` (JavaScript interactive dashboard). The file includes:
- Complete implementations of all 8 hypotheses tests
- Data processing and validation
- Interactive visualizations
- Downloadable results

**Note:** The protocol specifies WHAT to test (models, criteria). The implementation details HOW to test (code). This separation allows code evolution while maintaining protocol integrity.

---

## 7. ETHICS

### Informed Consent

**Information provided:**
- Study purpose: "Understanding perceptual decision-making"
- Procedure: "49 trials of color proportion judgment (~7 minutes)"
- Risks: None (minimal - standard cognitive task)
- Benefits: Contributes to cognitive science research
- Compensation: £1.80 (fair hourly rate)
- Withdrawal: Can exit at any time without penalty
- Data: Anonymous, stored securely, used for research only

**Consent required:**
- Explicit "I consent" checkbox in experiment
- Cannot proceed without consent

---

### Data Protection

**Anonymization:**
- No personal identifiable information collected
- Prolific PID stored separately from experimental data
- Session ID (UUID) used in analysis
- IP addresses NOT logged

**Storage:**
- Encrypted database (Azure SQL)
- Access restricted to research team
- Retained for 5 years (standard practice)
- Available on OSF upon publication

**GDPR Compliance:**
- Right to withdraw data (via Prolific PID, 7-day window)
- Data minimization (only task-relevant data collected)
- Purpose limitation (research only)

---

## 8. TIMELINE

| Phase | Duration | Activities |
|-------|----------|------------|
| **Pre-registration** | 1 week | OSF registration, final protocol review |
| **Pilot (N=5)** | 1 week | Test Prolific integration, check data pipeline |
| **Main collection** | 2-3 weeks | N=70 recruitment via Prolific |
| **Data cleaning** | 1 week | Apply exclusion criteria, validate data |
| **Analysis** | 2 weeks | Execute pre-registered tests + exploratory |
| **Manuscript** | 4 weeks | Write-up, visualizations, submission |

**Total estimated:** 10-12 weeks from pre-registration to submission

---

## 9. OPEN SCIENCE PRACTICES

### Pre-Registration

**Platform:** Open Science Framework (OSF)
**Contents:**
- Complete protocol (this document)
- Analysis code (JavaScript in dados.html)
- Exclusion criteria
- Statistical tests
- Validation criteria

**Timestamp:** Before data collection begins

---

### Data Sharing

**Upon publication:**
- Raw anonymized data (.csv)
- Analysis dashboard (dados.html - JavaScript)
- Experimental code (experimento.html)
- Figures and tables

**Repository:** OSF project page (DOI assigned)

---

### Code Availability

**GitHub repository:**
- Experiment code: `experimento.html`
- Analysis dashboard: `dados.html`
- Backend: ASP.NET Core
- Documentation: README with setup instructions

**License:** MIT (open source)

---

## 10. EXPECTED RESULTS

### Scenario 1: Full Validation (Most Likely)

**H1 confirmed + H3 (both H3a & H3b) confirmed**

**Interpretation:**
- HUMH accurately predicts RT structure
- Symbolic compression exists under finite maintenance resources (β > 0)
- Framework validated as meta-theory

**Publication:**
- "HUMH: Experimental Validation of Perceptual Convergence Dynamics"
- Target journals: Psychological Science, Cognition, JEP:General

---
  
### Scenario 2: Partial Validation (H1 confirmed, H3 not)
  
**Interpretation:**
- EH concept valid (RT reflects indefinition cost)
- BUT symbolic compression mechanism needs revision
- Core concepts (EH) still valuable
  
**Next steps:**
- Refine H3 implementation
- Test with different lag ranges
- Consider individual differences
  
---
  
### Scenario 3: Partial Validation (H3 confirmed, H1 not)

**Interpretation:**
- Compression mechanism valid (persistent representations despite β > 0)
- BUT EH structure not reflected in RT as predicted
- May indicate individual differences dominate

**Next steps:**
- Better EH operationalization
- Within-subjects design
- More granular EH levels

---

### Scenario 4: Falsification (Neither confirmed)
  
**Interpretation:**
- HUMH predictions not supported
- Framework needs major revision or abandonment

**Publication:**
- "Limits of the HUMH Framework: An Experimental Test"
- Valuable negative result (publish anyway!)

---

## 11. REFERENCES

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87-114.

Oppenheimer, D. M., Meyvis, T., & Davidenko, N. (2009). Instructional manipulation checks: Detecting satisficing to increase statistical power. *Journal of Experimental Social Psychology*, 45(4), 867-872.

Ratcliff, R., & McKoon, G. (2008). The diffusion decision model: Theory and data for two-choice decision tasks. *Neural Computation*, 20(4), 873-922.

---
    
## APPENDIX A: PROLIFIC STUDY TEXT
        
**Study Title:**  
Visual Perception Experiment - Color Proportion Judgment
            
**Study Description:**
```
You will complete a short visual perception task (7-10 minutes).
                
WHAT YOU'LL DO:
- View displays of blue and orange dots
- Decide which color appears MORE frequently
- Respond using keyboard arrow keys
- Complete 49 trials total
    
REQUIREMENTS:
- Desktop or laptop computer (NO mobile/tablet)
- Quiet environment recommended
- Fluent in English

COMPENSATION:
£1.80 for ~7-10 minutes (£15.43/hour rate)

Your responses are anonymous and contribute to cognitive science research.

Thank you for participating!
```

**Study Instructions (Prolific):**
```
1. Click the study link below
2. Read information sheet and provide consent
3. Complete the perception task (49 trials)
4. Answer brief post-experiment questions
5. You will receive a completion code: HUMH2025
6. Enter code on Prolific to receive payment

IMPORTANT:
- Use DESKTOP computer only (mobile blocked)
- Use LEFT/RIGHT arrow keys to respond
- Respond as quickly AND accurately as possible
- There are 2 simple attention checks included

Estimated time: 7-10 minutes
```

**Study URLs (Prolific Taskflow — balanced allocation 35/35):**

Prolific does NOT support a `{{%RANDOM_ALLOCATION%}}` placeholder (supported placeholders: PROLIFIC_PID, STUDY_ID, SESSION_ID). Group allocation uses **Taskflow** with two condition URLs; Taskflow distributes participants evenly and reallocates returned submissions:
```
Condition FV:
https://humh-deg8f0a6hzhtgyfu.brazilsouth-01.azurewebsites.net/experimento.html?PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}&group=FV

Condition SF:
https://humh-deg8f0a6hzhtgyfu.brazilsouth-01.azurewebsites.net/experimento.html?PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}&group=SF
```
The client (v1.2.1) validates the `group` parameter; any value outside {FV, SF} falls back to random assignment with a console warning.

**Completion URL:**
```
https://app.prolific.com/submissions/complete?cc=HUMH2025
```

---

## APPENDIX B: DATA DICTIONARY

| Variable | Type | Description | Values |
|----------|------|-------------|--------|
| `session_id` | UUID | Anonymous participant ID | e.g., "a1b2c3d4-..." |
| `prolific_pid` | String | Prolific participant ID | Stored separately |
| `group` | Factor | Experimental group | "FV", "SF" |
| `trial` | Integer | Trial number | 1-49 |
| `phase` | Factor | Experimental phase | "calibration", "training", "main" |
| `p_level` | Numeric | Proportion of blue dots | 0.09-0.91 |
| `rt_ms` | Numeric | Reaction time (milliseconds) | > 0 |
| `correct` | Boolean | Response accuracy | TRUE/FALSE |
| `choice_a` | Boolean | Chose blue (TRUE) or orange (FALSE) | TRUE/FALSE |
| `pair_id` | String | Paired trial identifier | "pair_X_Y_Z" or NULL |
| `is_attention_check` | Boolean | Trial is attention check | TRUE/FALSE |
| `timestamp` | Datetime | Trial completion time | ISO format |
| `keypress_log` | Array | All keypresses recorded | JSON array |

---

## APPENDIX C: PRE-REGISTRATION CHECKLIST

**Study Design:**
- [x] Between-subjects groups defined (FV vs SF)
- [x] Sample size justified (N=70, power analysis)
- [x] Inclusion/exclusion criteria specified
- [x] Recruitment platform confirmed (Prolific)

**Hypotheses:**
- [x] H1-H3 clearly stated with directional predictions
- [x] H4a-H4c exploratory hypotheses documented
- [x] Validation criteria pre-specified
- [x] Statistical tests pre-specified (JavaScript)

**Data Analysis:**
- [x] Pre-processing steps defined
- [x] Exclusion criteria objective and automatic
- [x] Analysis code provided (JavaScript in dados.html)
- [x] No researcher degrees of freedom

**Ethics:**
- [x] Informed consent procedure
- [x] Data protection measures
- [x] Fair compensation (£15.43/hour)

**Open Science:**
- [x] Pre-registration on OSF
- [x] Data sharing plan
- [x] Code availability (HTML/JavaScript)
- [x] Materials available

---

## APPENDIX D: TECHNICAL SPECIFICATIONS

### Experiment Implementation

**File:** `experimento.html`  
**Language:** HTML + JavaScript  
**Framework:** Vanilla JS (no external dependencies except Web Audio API)

**Key Features:**
- Deterministic spatial seed for pair identity
- Variable lag (1-3) for paired trials
- Web Audio API for multimodal feedback
- Prolific integration (PIDs, completion codes)
- Real-time backend logging

**Deployed at:** https://humh-deg8f0a6hzhtgyfu.brazilsouth-01.azurewebsites.net/

---

### Analysis Implementation

**File:** `dados.html`  
**Language:** HTML + JavaScript  
**Libraries:** 
- Plotly.js (visualization)
- jStat.js (statistical tests)

**Key Features:**
- Interactive dashboard
- Real-time hypothesis testing
- Automatic visualization generation
- Pre-registered analysis code embedded

**Accessible at:** Backend or local file

---

### Backend

**Technology:** ASP.NET Core + SQLite  
**Hosting:** Azure App Service  
**API Endpoint:** https://humh-api.azurewebsites.net/api/data

**Features:**
- CORS enabled for Prolific
- Real-time data storage
- RESTful API for data retrieval

---

**Document Version:** 1.4 FINAL (Visual Feedback Only)  
**Last Updated:** November 26, 2025  
**Status:** ✅ Ready for OSF Pre-registration

---

**For questions or clarifications:**  
Luciano Vianna  
Email: [contact information]  
OSF Project: [OSF link after registration]


---

## APÊNDICE A: FORMULAÇÃO MATEMÁTICA (da Teoria HUMH v1.7.0)

### 2.1.8.6 Aplicação no Experimento HUMH

**Contexto:**
Validação experimental dezembro 2025 com N=70 participantes.

**Formulação adotada: DISCRETA**

**Razão da escolha:**
1. Trials são unidade observável claramente discreta (n = 1, 2, ..., 49)
2. Não conhecemos τ_loop subjacente dos processos perceptivos individuais  
3. Trial é escala natural de análise (estímulo → resposta → feedback)
4. Dados coletados são inerentemente discretos (por trial)

**Notação experimental:**
```
n = trial_number  
p[n] = proporção de círculos brancos apresentados no trial n
EH[n] = 1 - |2p[n] - 1|
RT[n] = reaction time (ms) no trial n
acc[n] = accuracy (0/1) no trial n
phase[n] ∈ {1:calibration, 2:training, 3:main}
```

**Análises estatísticas em formulação discreta:**

**H1: EH → RT**
```
Modelo: RT[n] = α + β·EH[n] + ε[n]
Interpretação: β é slope por unidade de EH
Unidades: β em ms/EH (não ms/EH/segundo)
```

**H2: β > 0 (resistência observacional)**  
```
Modelo: RT[n] = α - β·lag[n] + ε[n]
Onde lag[n] = |EH[n-1] - EH[n]|
β medido por diferença de trials (não por segundo)
```

**H3: Facilitação em pares**
```
Comparação: RT[trial A] vs RT[trial B]
Onde trials A e B têm mesmo p mas diferentes n
Análise por trial (não por tempo contínuo)
```

**Conversão para taxa contínua (se necessário):**

Se desejarmos expressar β em unidades temporais contínuas:
```
τ_trial_médio = tempo_total_fase / número_trials ≈ 3 segundos

β_por_segundo ≈ β_por_trial / τ_trial_médio

Exemplo:
Se β_medido = 60 ms/trial
Então β_por_segundo ≈ 60/3 = 20 ms/segundo
```

**Importante:** Análise primária usa formulação discreta. Conversão 
contínua é opcional e apenas para interpretação comparativa.

---

---
