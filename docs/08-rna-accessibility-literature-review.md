# RNA region accessibility: literature review and additional constraints

**Audience note.** This is the evidence-heavy page. For definitions and
derivations first, read the [reading guide](00-reading-guide.md) and
[mathematical and chemical foundations](10-mathematical-and-chemical-foundations.md).
Paragraphs labeled **Deduction** or **Recommendation** are analytical
conclusions from the cited literature, not direct experimental claims.

RNA accessibility is conditional on the recognition mechanism, molecular environment, and timescale. The probability that a stretch is unpaired in an isolated RNA ensemble is a useful structural quantity, but it does not establish that an oligonucleotide can reach it, invade its neighboring structure, remain bound, or produce a biological response. These distinctions are supported by accessibility-aware interaction models, direct hybridization experiments, and recent measurements of dynamic RNA folding.[^rnaup][^interface][^gor]

This review addresses RNA targets in both purified reactions and cells, emphasizing recognition by complementary DNA or RNA strands, including protein-assisted recognition. It extends the repository's existing focus on joint unpaired probability, opening energy, nucleation seeds, and robustness. Published findings are cited; paragraphs marked **Deduction** or **Recommendation** are analytical conclusions or proposed practices rather than claims that a paper directly validated them. The companion [implementation proposal](09-rna-accessibility-implementation-proposal.md) maps these conclusions to `rnavail`.

The search was updated through 11 September 2026. It prioritized original method and experimental papers, including publisher records, PubMed records, and accessible full text; recent 2025–2026 studies were checked specifically. Sources were selected to test the repository's assumptions and cover distinct failure modes rather than to count every publication mentioning accessibility. This is an extensive critical review, not a registered systematic review or meta-analysis, so absence from the source list is not evidence that a factor is unimportant.

## 1. Define the event before estimating accessibility

### 1.1 Five quantities that should remain separate

| Quantity | Question answered | What it does not establish |
|---|---|---|
| Per-base unpaired probability | How often is nucleotide *k* unpaired in the modeled ensemble? | Whether a whole interval is open together |
| Joint interval unpaired probability | How often are all bases in interval *I* simultaneously unpaired? | A macromolecule's physical approach or binding rate |
| Geometric exposure | Is the relevant recognition surface exposed in a 3D conformation? | Whether the bases can form the desired duplex |
| Binding accessibility | Can a specified partner form an interaction under specified conditions? | Productive cleavage, switching, or regulation |
| Functional availability | Does that interaction produce the desired response during the observation period? | A transferable intrinsic property of the RNA sequence |

The first two are established ensemble observables; opening-energy methods connect the second to interaction thermodynamics. The last three require additional definitions and evidence. In particular, SHAPE reactivity measures local nucleotide dynamics, whereas hybridization assays interrogate access by a complementary strand. Neither measurement is interchangeable with a solvent-accessible surface calculation.[^raccess][^shape_dynamics][^interface]

For a fixed equilibrium secondary-structure model, let *Z* be its partition function and *Zᵤ(I)* the partition function restricted to structures in which every nucleotide of *I* is unpaired:

```text
Pᵤ(I) = Zᵤ(I) / Z
ΔGopen(I) = −RT ln Pᵤ(I) = Gᵤ(I) − G
```

Here *T* is absolute temperature and *R* must use units consistent with the energy. This is a free-energy difference between ensembles under the same model and constraints, not an activation barrier. RNAplfold instead supplies interval probabilities averaged across local windows; its transformed probability is not the mean of the windows' opening energies.[^raccess][^rnaplfold]

**Deduction.** Write the broader question as `P(recognition-compatible state | sequence, partner, environment, preparation, time)`. A scalar lacking this context cannot be a universal probability of successful targeting. For proteins or small molecules that recognize a folded motif, increased unpairing can even destroy the desired recognition state; the target event should follow the binder's mechanism.

### 1.2 Joint probability is essential, but complete pre-opening is not universally necessary

Marginal unpaired probabilities cannot reconstruct a joint interval probability without information about correlations. When all marginals refer to the same underlying ensemble, if the interval contains *L* bases with marginal probabilities *pₖ*, the elementary probability bounds are:

```text
max(0, Σpₖ − (L − 1)) ≤ Pᵤ(I) ≤ min(pₖ)
```

The product of the marginals assumes independence; their mean answers a different question. These are mathematical constraints, not empirical calibration rules. Also, bounds across different intervals need care when local methods average those intervals over different sets of windows.

Nevertheless, an oligonucleotide can nucleate on an exposed segment and extend while displacing existing structure. A low probability of the entire final footprint being pre-open therefore does not demonstrate that binding is impossible. Accessibility-aware interaction models and experiments on structured targets motivate reporting both full-region opening and pathway-relevant subregions.[^rnaup][^invasion][^larsen]

**Recommendation.** Interpret full-region opening as a structural cost or a strict pre-open event. Describe the best seed as a hypothesis about where binding might start. Avoid presenting either as a necessary and sufficient rule for all binders.

## 2. Binding pathways, partner identity, and time

### 2.1 The best exposed seed may not be a usable nucleation site

Seed length, complementarity, position, mismatches, and hybridization energy can all affect recognition. An IntaRNA benchmark found that changing seed and interaction constraints materially changed bacterial sRNA target recovery, with some recommendations dependent on the thermodynamic parameterization. This supports mechanism-specific settings rather than a universal 10-nucleotide seed.[^seed_constraints]

**Deduction.** Maximizing seed accessibility over every position is optimistic if a fixed probe can initiate only at one end, a guide has positional requirements, or the relevant seed must be exposed on both partners. A favorable internal seed also does not establish that extension can cross a stable helix, a junction, or a mismatch. Record each tested seed's coordinates, orientation, length, and whether the search was exhaustive.

Coarse-grained simulations of simple toehold-mediated RNA strand-displacement systems found dependence on toehold length, terminal placement, and temperature, with a modeled 5′/3′ asymmetry arising from RNA geometry and cross-stacking. This result supports retaining orientation and pathway information, but its numerical trends should not be treated as universal cutoffs for native transcripts.[^oxrna]

Recent Cas13 experiments make this distinction concrete. Larsen and colleagues found that protospacer structure impeded activity in a manner explained by strand displacement. Structure immediately 3′ of the protospacer could inhibit activity despite retaining strong target binding, separating recognition from downstream activation. The study concerns the tested Cas13 system and assay designs, not every RNA-targeting effector.[^larsen]

**Recommendation.** Use separate labels for paired recognition footprint, possible nucleation footprint, and surrounding steric or functional context. A generic “20-nt sgRNA” rule is unsuitable for RNA accessibility: commonly used Cas9 guides target DNA, while RNA-targeting effectors have their own spacer and recognition requirements.

### 2.2 Opening energy is only one thermodynamic contribution

Accessibility-aware interaction models combine opening penalties with favorable intermolecular pairing. A useful schematic decomposition is:

```text
ΔGinteraction,model ≈ ΔGopen,target + ΔGopen,partner + ΔGintermolecular
```

The precise definition depends on the interaction model, including its initiation and loop terms. This decomposition does not by itself yield a kinetic rate or equilibrium occupancy at a specified concentration.[^rnaup][^intarna]

DNA/RNA hybrids require appropriate hybrid parameters. Sugimoto and colleagues measured distinct RNA/DNA nearest-neighbor terms, and Banerjee and colleagues later developed parameters for lower-salt conditions. The latter study has a published correction that must accompany any parameter implementation. RNA/RNA or DNA/DNA tables should not silently substitute for hybrid chemistry.[^hybrid1995][^hybrid2020]

**Deduction.** `--molecule dna` describes a DNA *target* in this repository; it cannot stand in for “DNA probe binding an RNA target.” Modified probes additionally require chemistry-specific support. Until such support exists, retain the target's RNA opening calculation and mark partner binding thermodynamics as unmodeled.

### 2.3 Identical equilibrium accessibility can conceal different kinetics

For an illustrative two-state RNA, `closed ⇌ open`, equilibrium openness is `kopen / (kopen + kclose)`. Multiplying both rates by the same factor leaves that probability unchanged while changing the dwell times. This mathematical example shows why an equilibrium score cannot tell whether a transient opening lasts long enough for capture.

Experiments and modeling on short, deliberately weakly structured RNA mixtures distinguished association, dissociation, and strand-displacement rates and found that competition could retain out-of-equilibrium populations for minutes to hours. These fitted rates do not transfer directly to long structured transcripts, but the experiment demonstrates that favorable complexes and fast arrival are different properties.[^kinetics]

Real RNAs also remember their preparation. Cotranscriptional folding restricts which segments are available at each time and can generate pathways different from refolding a completed transcript. Direct single-molecule work in a purified, surface-immobilized cotranscriptional 16S-rRNA-domain system resolved distinct nascent RNA folding classes and their responses to proteins and oligonucleotides.[^cotranscription][^gor]

**Deduction.** Record whether the RNA was transcribed with the binder present, heat-refolded, purified and refolded, extracted from cells, or observed in situ. Record incubation time and free partner concentration. These variables can explain rank changes without any change in sequence or equilibrium secondary-structure prediction.

### 2.4 The binder can change what is being measured

In an in-vitro iSAT ribosome-assembly system and S150 extract, Sheng and colleagues showed that antisense oligonucleotides can capture ribosomal assembly intermediates. In a purified nascent-rRNA system, Gor and colleagues found that intentional antisense oligonucleotides and other factors redistributed subsets of folding classes; their short reporting probes were separately tested for detectable perturbation in that assay. Accessibility measurements with a binder can therefore perturb the ensemble rather than passively report its unbound state.[^sheng][^gor]

**Recommendation.** Distinguish unliganded structural probing, initial association, and the bound or functionally altered endpoint. A long incubation or high probe concentration may reveal a capturable site that was rarely open before probe addition. That is useful evidence, but it measures a different event from spontaneous full-region opening.

## 3. Structural constraints beyond ordinary secondary structure

### 3.1 Tertiary contacts and approach geometry

Unpaired bases can participate in tertiary contacts or occupy a compact environment with limited access by a large partner. Experiments on a group I ribozyme showed that a tetraloop–receptor interaction altered folding accuracy and kinetic partitioning beyond the locally changed motif. Conversely, an RNA can be globally compact while exposing a particular loop. Chemical probing, a predicted secondary structure, and 3D exposure therefore provide complementary structural information.[^tertiary][^shape_dynamics][^martini]

**Deduction.** Local base-face exposure, proximity of obstructing RNA or protein, and the direction from which a duplex must approach are more relevant than whole-molecule radius of gyration. A solvent-sized probe used for SASA is not an oligonucleotide or a Cas complex. SASA should be an auxiliary geometric descriptor, with the atom selection and probe radius stated.

### 3.2 Pseudoknots and omitted states do not imply a universal error direction

ProbKnot can predict crossing base pairs from pairing probabilities, but a predicted pseudoknotted structure is not a partition function over pseudoknotted conformations. It can provide a structural hypothesis that a nested model misses; it cannot calibrate the probability that the target is blocked by that hypothesis.[^probknot]

**Deduction.** “Adding missing structures always decreases accessibility” is not generally valid. Adding states changes both the partition function and the target-open numerator. Added states that pair the target can reduce accessibility; added states that sequester a competing segment elsewhere can increase it. Thus a missing topology is model uncertainty, not automatically a signed penalty. The same reasoning prevents treating every local-versus-global discrepancy as proof of long-range burial.

### 3.3 G-quadruplex propensity is conditional evidence

G-rich sequence motifs are not equivalent to occupied RNA G-quadruplexes. Guo and Bartel found that many regions capable of forming RNA G-quadruplexes in vitro were predominantly unfolded in eukaryotic cells. This does not establish that cellular RNA G-quadruplexes never occur; it establishes that sequence potential and cellular occupancy can differ substantially.[^gquad]

**Recommendation.** Keep motif propensity, predicted G-quadruplex structure, and experimentally supported occupancy as separate evidence types. Specify the ionic and biological context. If a folding model includes G-quadruplexes, explicitly verify that its “target unpaired” constraint also excludes participation in a quadruplex; absence of ordinary base pairs alone is insufficient.

### 3.4 Full transcript context and topology

RNA duplex mapping in cells has revealed long-range and alternative structures. Truncating the input can remove real pairing partners or create artificial boundaries. Comparisons of global and local mRNA folding found that performance depended on window and span choices and that artificial sequence ends could distort accessibility. A local window can still be useful computationally, but it represents a different conditional model from the intact transcript.[^paris][^local_context][^rnaplfold]

**Deduction.** Compare the exact expressed construct, plausible transcript isoforms, and local contexts with explicit coordinate maps. Include UTRs and designed flanks when relevant. Circular RNA requires a topology-aware model and intervals spanning the ligation junction; simply concatenating arbitrary sequence pieces or treating the RNA as linear can change the modeled event. Context sensitivity is evidence of uncertainty, not a correction that always shifts in one direction.

## 4. Solution conditions and chemical state

### 4.1 Ions are more than a scalar salt concentration

Measurements on a pseudoknot and an rRNA fragment found that Mg²⁺ interaction free energies depend on the RNA and conformation, including partially unfolded states. Experiments on a group I ribozyme also show that macromolecular crowding can shift Mg²⁺-dependent compaction and folding.[^magnesium][^crowding] **Deduction.** A scalar monovalent-ion correction does not represent specific divalent binding, every ion-mediated tertiary contact, or the distinction between free and total Mg²⁺. The relevant comparison is between the model's supported conditions and the actual preparation.

**Recommendation.** Record Na⁺, K⁺, total Mg²⁺, any measured or estimated free Mg²⁺, temperature, pH, and relevant ligands or chelators. Mark unsupported variables as unmodeled. Do not translate Mg²⁺ into an “equivalent monovalent salt” without a validated model for the particular molecular system.

### 4.2 Crowding is not a universal accessibility penalty

Kilburn and colleagues demonstrated crowding-assisted folding of a ribozyme at lower magnesium concentrations than were needed without the crowder. Such experiments establish that dilute-solution assumptions can fail, but a result for one RNA and crowder does not supply a universal correction for every target, interaction, or cellular environment.[^crowding]

**Deduction.** Even when crowding favors compact conformations, its effect on a particular target interval depends on which conformations are favored and how diffusion and nonspecific interactions change. Record crowder identity and concentration, and compare matched experiments. Do not assign a fixed negative score to every cellular or crowded sample.

### 4.3 Modifications and protonation can alter local recognition

Liu and colleagues demonstrated an m⁶A-dependent structural switch that changes access of an RNA-binding protein to an RNA motif. This establishes a mechanism by which an RNA with the same canonical sequence can acquire a different recognition landscape. It does not justify assuming that every methylated position is more accessible.[^m6a]

**Deduction.** A canonical FASTA is incomplete when modification identity or stoichiometry matters. Treat known modifications as site-specific annotations with evidence and sample context; an unmodified reference fold is a counterfactual baseline. Likewise, a pH change can affect chemical probing and molecular interactions, so changing pH should not be simulated by a temperature change or an arbitrary opening-energy offset.

## 5. Cellular accessibility includes occupancy and active remodeling

### 5.1 Cellular structure is not uniformly more open or more closed

Rouskin and colleagues observed far fewer structured mRNA regions in rapidly dividing yeast and mammalian cells than after in-vitro refolding; ATP depletion increased mRNA structure in yeast. Mustoe and colleagues found substantial structure in the *E. coli* mRNAs they assayed and examined translation-associated remodeling. These studies differ in organism, transcript coverage, probe, and experimental context; neither provides a universal cellular scaling factor.[^rouskin][^mustoe]

**Recommendation.** Prefer evidence from the same organism, cell type, growth or stress condition, and compartment. Keep in-cell and in-vitro profiles as separate conditions. An experimental discrepancy should generate a biological hypothesis rather than be averaged away.

### 5.2 Proteins can occlude, stabilize, or assist recognition

The INTERFACE study measured regional hybridization accessibility of bacterial sRNAs in vivo and examined how Hfq affected it. Its findings support both the relevance of protein context and the value of direct hybridization evidence. Protein binding is not always an obstacle: RNA chaperoning can create or maintain useful interaction states.[^interface]

eCLIP supplies evidence of protein–RNA interaction sites under specified experimental conditions.[^eclip] **Deduction.** Its enrichment signal is not itself a fractional occupancy measurement for every molecule, and an absent peak is not evidence that the interval is protein-free.

**Deduction.** Overlapping protein-binding evidence should be an annotation or a condition-specific model feature. It should not automatically multiply target accessibility by an invented “unoccupied fraction.” Protein identity, matched expression, condition, and whether binding assists or competes with the intended partner all matter.

### 5.3 Translation creates moving opportunities and obstacles

Ribosome-associated remodeling links RNA structure to translation, and cellular structure experiments show that its effects depend on local translation and structural context.[^mustoe] **Deduction.** An occupying ribosome can also obstruct another large complex, so remodeling and steric competition can act in opposite directions.

**Deduction.** Ribosome profiling can locate translated regions and pauses, but average read density alone does not determine the duration of an accessible interval between ribosomes. A highly translated CDS can be repeatedly remodeled and repeatedly occluded. Treat net accessibility as unresolved unless binder-specific data constrain the competition.

### 5.4 Isoforms, variants, and compartments define different targets

Subcellular structure mapping demonstrated RNA structural differences across cellular compartments and links to RNA processing and protein interaction. More recent direct RNA sequencing resolved isoform-specific structural ensembles along SARS-CoV-2 RNAs and heterogeneous ensembles across the *Candida albicans* transcriptome. Gene-level sequence or expression summaries can therefore hide structurally distinct RNA populations.[^compartment][^nanopore2026]

**Recommendation.** Identify the transcript version and sequence, not only the gene. Map the target across relevant splice and end-processing isoforms; distinguish absent sites from poorly accessible sites. Evaluate observed variants separately from arbitrary mutational sensitivity tests. An expression-weighted accessible amount is a new, context-dependent estimate and requires credible isoform abundance and co-localization data.

## 6. Experimental evidence: what each assay can support

### 6.1 Reactivity is not a calibrated probability of macromolecular access

SHAPE reactivity reflects local conformational dynamics and is not a direct measure of solvent accessibility. Low reactivity can be compatible with several constrained environments.[^shape_dynamics] **Deduction.** High reactivity alone does not guarantee that a complementary oligonucleotide can form a productive duplex.

DMS information depends on the chemistry and analysis. Common protocols primarily exploit A/C reactivity, but four-base DMS methods can recover additional structural information under appropriate conditions and filtering. A pipeline must know which protocol produced the numbers rather than assuming every DMS track has the same base coverage.[^dms4]

Experiment-derived accessibility profiles can be incorporated into accessibility-aware RNA–RNA interaction prediction, as demonstrated in an IntaRNA extension. That method establishes a way to condition a computational interaction model; it does not turn the reactivity itself into a direct probability of binding.[^probing_interaction]

**Recommendation.** Preserve chemistry, preprocessing, normalization, nucleotide coverage, missing-value masks, replicate identifiers, transcript mapping, and condition metadata. Missing reactivity must remain missing. A SHAPE-to-pseudoenergy conversion is not automatically appropriate for arbitrary DMS data.

### 6.2 Ensemble averages can hide mutually exclusive conformations

DREEM demonstrated the extraction of distinct RNA structural populations from single-molecule chemical probing data. The 2026 direct-RNA-sequencing study resolved isoform-specific ensembles along SARS-CoV-2 RNA and heterogeneous ensembles in the *Candida albicans* transcriptome. These results support treating a mean reactivity profile as a projection of a population, rather than a single structure.[^dreem][^nanopore2026]

**Deduction.** If distinct states expose different parts of a target, the mean profile can look broadly reactive even when no abundant state exposes the full interval. When state-resolved data are available, calculate accessibility within each inferred state and retain state proportions and uncertainty. Do not multiply mean reactivities to estimate joint openness.

### 6.3 A hierarchy of evidence matched to the question

| Evidence | Most appropriate use | Main interpretation limit |
|---|---|---|
| SHAPE/DMS with matched conditions | Inform structural ensembles; identify local differences | Chemistry-dependent, often averaged over molecules |
| State-resolved probing | Identify alternative conformations and mixtures | Inference and read coverage limit identifiable states |
| PARIS or related duplex mapping | Support particular long-range or alternative contacts | Detected contact does not establish its complete occupancy |
| eCLIP or related protein maps | Identify plausible RNP competition or assistance | Enrichment is not a calibrated vacant-site probability |
| Direct hybridization mapping | Test regional access by a complementary strand | Probe sequence, chemistry, dose, and exposure time matter |
| Association/dissociation measurements | Test rates and bound-state persistence | Assay and immobilization conditions may alter behavior |
| Functional assay | Test the intended design outcome | Includes delivery, abundance, binding, and downstream mechanisms |

The distinctions in this table follow the measurement definitions and demonstrations in the cited studies; the proposed hierarchy is a recommendation, not a cross-assay accuracy ranking.[^interface][^eclip][^dreem][^paris]

An early native-mRNA study is particularly instructive: Scherr and Rossi found that oligonucleotide-directed RNase H assays in cell extracts discriminated sites differently from a purified in-vitro transcript, and the native-context ranking better matched cellular effects for their tested target. RNase H cleavage still includes enzyme access and catalysis, so it is not a pure measurement of unbound-state openness.[^scherr]

## 7. Computational uncertainty and score interpretation

### 7.1 Numerical agreement is distinct from biological calibration

EternaBench showed that packages differ on ensemble-sensitive experimental tasks and that training on diverse measurements can improve performance. The study also showed that temperature handling differs among packages and identified explicit ionic-condition and temperature modeling as future work.[^eterna] **Deduction.** Probabilities from a learned energy model are useful predictions, but they should not be treated as transferable physical free energies at temperatures or ionic conditions the model does not represent.

**Deduction.** Multiple tools using related parameter tables and structural assumptions share model errors. Agreement between a library and its command-line interface is valuable implementation validation, but adds no independent biological evidence. Likewise, exact constrained partition functions and sampling from the same model are alternative estimators of a shared model, not independent experiments.

A 2025 benchmark compared 23 RNA–RNA interaction methods using contacts in experimentally determined complexes. That endpoint is inter-RNA base-pair prediction, not live-cell accessibility, binding kinetics, or gate output. A tool's benchmark position must be interpreted against the task actually evaluated.[^benchmark2025]

### 7.2 Local models, global models, and “exact” calculations

RNAplfold averages interval probabilities over windows and restricts base-pair span. A full-sequence calculation can also retain a span limit. “Exact” therefore means exact for the stated model and constraints, not exact for the physical RNA.[^rnaplfold]

**Deduction.** For comparable local probabilities at one temperature, Jensen's inequality gives `−RT ln(mean(P)) ≤ mean(−RT ln(P))`. The distinction is mathematically predictable, not a rounding error. Moreover, local-versus-global differences can reflect window weighting, boundaries, permitted pairing partners, and mismatched settings; their sign does not identify a unique molecular mechanism.

### 7.3 Avoid counting transformed metrics as separate evidence

**Deduction.** For one interval and one temperature, `Pᵤ` and `ΔGopen` are deterministic transforms. At fixed length, `ΔGopen/length` is another transform. Giving all three independent-looking weights can overweight one structural signal. Averaging probabilities and energies separately can also produce a headline pair that violates their defining relation, especially when an even-number median averages the middle two values.

The same issue affects seed summaries: different tools may choose different seed coordinates. A median of their best probabilities is not the probability of one common seed. Preserve per-seed identity or evaluate a shared seed set before comparing tools.

### 7.4 Rare events, entropy, and robustness have specific meanings

**Deduction.** Observing zero open structures in *N* independent samples does not prove zero probability. The one-sided 95% binomial upper bound is `1 − 0.05^(1/N)`, approximately `3/N`. Correlated trajectory frames require an effective sample size or an appropriate time-series uncertainty analysis; simply counting frames understates uncertainty.

High ensemble entropy need not mean high accessibility: a region can vary among many paired conformations, while a consistently unpaired loop can have low pairing-state entropy. For the usual Boltzmann model, `P(MFE) = exp(−(G_MFE − G_ensemble)/RT)` for the corresponding state. A small gap indicates high MFE-state weight, not a diffuse ensemble.

**Recommendation.** Separate sampling uncertainty, model disagreement, condition sensitivity, and biological variability. Robustness across a chosen sweep establishes stability under that sweep, not a calibrated confidence interval or proof of cellular availability.

## 8. Three-dimensional modeling and the existing CGMD proposal

The existing [Katzir-inspired background document](../RNA_Target_Region_Accessibility_Katzir_CGMD.md) usefully motivates geometric exposure analysis. However, Katzir and colleagues studied programmable ssDNA and condensate behavior. Transferring its structural descriptors to RNA targeting is a proposed analogy, not evidence that a specific RNA availability score predicts hybridization or function.[^katzir]

The Martini RNA model of Yangaliev and Ozkan was published online in 2025 and in a 2026 journal issue. It demonstrates properties of individual bases, ssRNA, dsRNA, and RNA–protein complexes; for complex configurations such as tRNA, it incorporates an elastic network to maintain structural integrity. Such restraints are material to interpreting whether a simulation can sample the opening event of interest.[^martini]

**Deduction.** A trajectory cannot establish spontaneous target melting if the topology or restraints prevent the relevant base-pair or tertiary rearrangement. Many replicas of the same constrained basin do not solve this representational limitation. A useful first question is whether the model can represent and has been validated for the event, followed by whether the simulations sample it.

**Recommendation.** Use CGMD as a later, separately validated structural analysis for selected candidates. Preserve starting structures, topology, restraints, force-field version, ion treatment, replica details, and target-specific exposure distributions. Treat thresholded `f_available` values as model- and threshold-dependent descriptors; no universal cutoff such as 0.5–0.7, universal physical clock conversion, or candidate throughput is established by the cited studies. The cited oxRNA strand-displacement study models RNA–RNA systems; the later oxNA model extends coarse-grained modeling to DNA–RNA hybrids. Both still require validation for the intended target, chemistry, and conditions.[^oxrna][^oxna_hybrid]

## 9. Additional constraints to retain for each candidate

The following is a proposed decision framework derived from the evidence above. “Unknown” should remain an explicit state rather than becoming either a zero penalty or a fabricated probability.

| Constraint or consideration | Record or compare | Priority |
|---|---|---|
| Exact molecular identity | Full target sequence, transcript/construct version, topology, coordinates | Every run |
| Recognition mechanism | Full footprint, allowed seed positions, orientation, partner chemistry | Every interpreted shortlist |
| Estimand and model | Joint versus marginal; local versus full sequence; span; parameters | Every numeric result |
| Experimental conditions | Temperature, ions, pH, preparation, assay time | Every run; flag unmodeled fields |
| Probing provenance | Assay chemistry, mapping, coverage, condition, whether applied | Whenever data exist |
| Conformational heterogeneity | State-specific accessibility and state proportions | When identifiable from data |
| Binding kinetics | Association, dissociation, dwell times, order of addition | Before treating scores as performance |
| RNP environment | Relevant protein and ribosome evidence with context | Cellular applications |
| RNA modifications | Positions, chemistry, stoichiometry, evidence | Modified or endogenous targets |
| Structural alternatives | Long-range contacts, pseudoknots, G-quadruplex evidence | Diagnostic layer |
| Sequence and context uncertainty | Observed variants, isoforms, flanks, truncation sensitivity | Biological target selection |
| Partner and competitor effects | Partner self-structure, chemistry, concentrations, competing targets | Optional interaction layer |
| Tertiary approach geometry | Target surface, obstructing contacts, permitted rearrangements | Selected difficult cases |
| Confidence and missingness | Sampling limits, supported settings, model families, unmeasured biology | Every report |

## 10. Validation that can distinguish explanations

**Recommendation.** Select a diverse experimental panel rather than only the top-scoring intervals: low and high opening costs, disagreement between local and full-sequence models, plausible G-quadruplex or protein effects, and strong differences between full-region and seed accessibility. Include different transcripts and structural contexts so the panel tests transferability.

Measure structure and direct binding under matched conditions, followed by the intended functional endpoint. Use concentration and time series to distinguish weak equilibrium binding from slow capture. Compare intact and truncated RNA only as an explicit context perturbation. Where feasible, disrupt a predicted competing helix outside the recognition sequence and restore it with a compensatory change; changes within the recognition sequence confound structure with complementarity.

For cellular applications, matched purified-RNA, extract, and cellular measurements can locate where the discrepancy enters. These are different biological preparations, not interchangeable ground truths. Interpret enzyme-based outputs alongside direct binding where possible, given the demonstrated separation of binding and activity.[^scherr][^larsen]

**Deduction.** Evaluation splits should separate related transcripts and overlapping target windows; otherwise nearly identical regions can occur in training and testing. Fit ranking weights only against a declared endpoint, retain simple opening-energy baselines, and test whether added features improve held-out ranking or calibration. A calibrated functional success model would be a new empirical model, not a renamed thermodynamic accessibility score.

## 11. Statements that need qualification in the existing documentation

| Existing simplifying idea | More defensible interpretation |
|---|---|
| The entire footprint must already be open for binding | Full opening defines one event; nucleation and displacement can use a different pathway |
| An open site is necessarily physically reachable | Secondary-structure openness does not establish steric approach or vacant protein occupancy |
| Omitted pseudoknots, tertiary contacts, or longer-range pairs only overestimate openness | Missing states can redistribute the ensemble in either direction |
| Whole-sequence “exact” is the unconstrained physical reference | Exactness is conditional on parameters, span limits, included topologies, and applied data |
| More tools imply independent evidence | Interfaces, estimators, and shared parameter families can be strongly dependent |
| More crowding or protein binding always reduces access | Local effects can increase or decrease recognition compatibility |
| SHAPE/DMS measurements directly provide availability | Assays measure chemistry-specific observables that require interpretation and mapping |
| Higher entropy necessarily means more available RNA | Entropy describes variability, not whether the desired target event occurs |
| A CGMD frame fraction is a calibrated binding probability | It is a conditional descriptor until the represented event and experimental relationship are validated |

These revisions preserve the usefulness of the existing target-RNA ensemble approach while making its assumptions testable. The immediate implementation priorities are defined in the [companion proposal](09-rna-accessibility-implementation-proposal.md).

## Sources

[^raccess]: Bernhart SH, Mückstein U, Hofacker IL. “[RNA Accessibility in cubic time](https://doi.org/10.1186/1748-7188-6-3).” *Algorithms for Molecular Biology* 6, 3 (2011); Kiryu H, Terai G, Imamura O, et al. “[A detailed investigation of accessibilities around target sites of siRNAs and miRNAs](https://doi.org/10.1093/bioinformatics/btr276).” *Bioinformatics* 27, 1788–1797 (2011).

[^rnaplfold]: Bernhart SH, Hofacker IL, Stadler PF. “[Local RNA base pairing probabilities in large sequences](https://doi.org/10.1093/bioinformatics/btk014).” *Bioinformatics* 22, 614–615 (2006); ViennaRNA. “[RNAplfold manual, version 2.7.2](https://www.tbi.univie.ac.at/RNA/ViennaRNA/doc/html/man/RNAplfold.html).” Accessed 11 September 2026. The software manual is included because it defines the current window-averaged output used by the repository.

[^rnaup]: Mückstein U, Tafer H, Hackermüller J, Bernhart SH, Stadler PF, Hofacker IL. “[Thermodynamics of RNA–RNA binding](https://doi.org/10.1093/bioinformatics/btl024).” *Bioinformatics* 22, 1177–1182 (2006).

[^invasion]: Serikov R, Petyuk V, Vorobijev Y, et al. “[Mechanism of antisense oligonucleotide interaction with natural RNAs](https://doi.org/10.1080/073911011010524987).” *Journal of Biomolecular Structure and Dynamics* 29, 27–50 (2011).

[^larsen]: Larsen BB, Kimchi O, Dunkley ORS, et al. “[RNA structure modulates Cas13 activity and enables mismatch detection](https://doi.org/10.1038/s41587-025-02868-6).” *Nature Biotechnology* (2025), PMID [41131153](https://pubmed.ncbi.nlm.nih.gov/41131153/).

[^seed_constraints]: Raden M, Müller T, Mautner S, Gelhausen R, Backofen R. “[The impact of various seed, accessibility and interaction constraints on sRNA target prediction—a systematic assessment](https://doi.org/10.1186/s12859-019-3143-4).” *BMC Bioinformatics* 21, 15 (2020).

[^hybrid1995]: Sugimoto N, Nakano S, Katoh M, et al. “[Thermodynamic parameters to predict stability of RNA/DNA hybrid duplexes](https://doi.org/10.1021/bi00035a029).” *Biochemistry* 34, 11211–11216 (1995).

[^hybrid2020]: Banerjee D, Tateishi-Karimata H, Ohyama T, et al. “[Improved nearest-neighbor parameters for the stability of RNA/DNA hybrids under a physiological condition](https://doi.org/10.1093/nar/gkaa572).” *Nucleic Acids Research* 48, 12042–12054 (2020); correction: Banerjee D, Tateishi-Karimata H, Ohyama T, et al. “[Correction to ‘Improved nearest-neighbor parameters…’](https://doi.org/10.1093/nar/gkab780).” *Nucleic Acids Research* 49, 10796–10799 (2021).

[^intarna]: Mann M, Wright PR, Backofen R. “[IntaRNA 2.0: enhanced and customizable prediction of RNA–RNA interactions](https://doi.org/10.1093/nar/gkx279).” *Nucleic Acids Research* 45, W435–W439 (2017).

[^cotranscription]: Watters KE, Strobel EJ, Yu AM, Lis JT, Lucks JB. “[Cotranscriptional folding of a riboswitch at nucleotide resolution](https://doi.org/10.1038/nsmb.3316).” *Nature Structural & Molecular Biology* 23, 1124–1131 (2016).

[^gor]: Gor K, Geissen EM, Duss O. “[Functional characterization of dynamic nascent RNA folding ensembles in real time](https://doi.org/10.1126/sciadv.aec4037).” *Science Advances* 12, eaec4037 (2026), [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13004024/).

[^sheng]: Sheng K, Dong X, Aiyer S, et al. “[Anti-sense oligonucleotide probing as a structural platform for studying ribonucleoprotein complex assembly](https://doi.org/10.1038/s41467-025-61640-1).” *Nature Communications* 16, 6642 (2025).

[^shape_dynamics]: McGinnis JL, Dunkle JA, Cate JHD, Weeks KM. “[The mechanisms of RNA SHAPE chemistry](https://doi.org/10.1021/ja2104075).” *Journal of the American Chemical Society* 134, 6617–6624 (2012).

[^probknot]: Bellaousov S, Mathews DH. “[ProbKnot: fast prediction of RNA secondary structure including pseudoknots](https://doi.org/10.1261/rna.2125310).” *RNA* 16, 1870–1880 (2010).

[^gquad]: Guo JU, Bartel DP. “[RNA G-quadruplexes are globally unfolded in eukaryotic cells and depleted in bacteria](https://doi.org/10.1126/science.aaf5371).” *Science* 353, aaf5371 (2016); Kharel P, Fay M, Manasova EV, et al. “[Stress promotes RNA G-quadruplex folding in human cells](https://doi.org/10.1038/s41467-023-35811-x).” *Nature Communications* 14, 205 (2023). The second study is included to bound the first study's generality across cellular conditions.

[^paris]: Lu Z, Zhang QC, Lee B, et al. “[RNA duplex map in living cells reveals higher-order transcriptome structure](https://doi.org/10.1016/j.cell.2016.04.028).” *Cell* 165, 1267–1279 (2016).

[^crowding]: Kilburn D, Roh JH, Guo L, Briber RM, Woodson SA. “[Molecular crowding stabilizes folded RNA structure by the excluded volume effect](https://doi.org/10.1021/ja101500g).” *Journal of the American Chemical Society* 132, 8690–8696 (2010).

[^magnesium]: Grilley D, Soto AM, Draper DE. “[Mg²⁺–RNA interaction free energies and their relationship to the folding of RNA tertiary structures](https://doi.org/10.1073/pnas.0606409103).” *Proceedings of the National Academy of Sciences USA* 103, 14003–14008 (2006); Yamagami R, Bingaman JL, Frankel EA, Bevilacqua PC. “[Cellular conditions of weakly chelated magnesium ions strongly promote RNA stability and catalysis](https://doi.org/10.1038/s41467-018-04415-1).” *Nature Communications* 9, 2149 (2018).

[^m6a]: Liu N, Dai Q, Zheng G, He C, Parisien M, Pan T. “[N6-methyladenosine-dependent RNA structural switches regulate RNA–protein interactions](https://doi.org/10.1038/nature14234).” *Nature* 518, 560–564 (2015); Liu B, Merriman DK, Choi SH, et al. “[A potentially abundant junctional RNA motif stabilized by m6A and Mg2+](https://doi.org/10.1038/s41467-018-05243-z).” *Nature Communications* 9, 2761 (2018). The second study establishes that the structural effect can depend on motif and Mg²⁺ context.

[^rouskin]: Rouskin S, Zubradt M, Washietl S, Kellis M, Weissman JS. “[Genome-wide probing of RNA structure reveals active unfolding of mRNA structures in vivo](https://doi.org/10.1038/nature12894).” *Nature* 505, 701–705 (2014).

[^mustoe]: Mustoe AM, Busan S, Rice GM, et al. “[Pervasive regulatory functions of mRNA structure revealed by high-resolution SHAPE probing](https://doi.org/10.1016/j.cell.2018.02.034).” *Cell* 173, 181–195.e18 (2018).

[^interface]: Mihailovic MK, Vazquez-Anderson J, Li Y, et al. “[High-throughput in vivo mapping of RNA accessible interfaces to identify functional sRNA binding sites](https://doi.org/10.1038/s41467-018-06207-z).” *Nature Communications* 9, 4084 (2018).

[^eclip]: Van Nostrand EL, Pratt GA, Shishkin AA, et al. “[Robust transcriptome-wide discovery of RNA-binding protein binding sites with enhanced CLIP (eCLIP)](https://doi.org/10.1038/nmeth.3810).” *Nature Methods* 13, 508–514 (2016).

[^compartment]: Sun L, Fazal FM, Li P, et al. “[RNA structure maps across mammalian cellular compartments](https://doi.org/10.1038/s41594-019-0200-7).” *Nature Structural & Molecular Biology* 26, 322–330 (2019).

[^nanopore2026]: Wang J, Han J, Tan WT, et al. “[Direct RNA sequencing and signal alignment reveal RNA structure ensembles in a eukaryotic cell](https://doi.org/10.1038/s41592-026-03069-y).” *Nature Methods* 23, 914–923 (2026).

[^dms4]: Mitchell D III, Cotter J, Saleem I, Mustoe AM. “[Mutation signature filtering enables high-fidelity RNA structure probing at all four nucleobases with DMS](https://doi.org/10.1093/nar/gkad522).” *Nucleic Acids Research* 51, 8744–8757 (2023).

[^dreem]: Tomezsko PJ, Corbin VDA, Gupta P, et al. “[Determination of RNA structural diversity and its role in HIV-1 RNA splicing](https://doi.org/10.1038/s41586-020-2253-5).” *Nature* 582, 438–442 (2020); correction [10.1038/s41586-020-2949-6](https://doi.org/10.1038/s41586-020-2949-6).

[^scherr]: Scherr M, Rossi JJ. “[Rapid determination and quantitation of the accessibility to native RNAs by antisense oligodeoxynucleotides in murine cell extracts](https://doi.org/10.1093/nar/26.22.5079).” *Nucleic Acids Research* 26, 5079–5085 (1998).

[^eterna]: Wayment-Steele HK, Kladwang W, Strom AI, et al. “[RNA secondary structure packages evaluated and improved by high-throughput experiments](https://doi.org/10.1038/s41592-022-01605-0).” *Nature Methods* 19, 1234–1242 (2022).

[^benchmark2025]: Lang M, Litfin T, Chen K, Zhan J, Zhou Y. “[Benchmarking the methods for predicting base pairs in RNA–RNA interactions](https://doi.org/10.1093/bioinformatics/btaf289).” *Bioinformatics* 41, btaf289 (2025).

[^katzir]: Katzir I, Wen Y, Razi I, et al. “[Programmable DNA folding modulates phase behavior and dynamics of DNA/peptide condensates](https://doi.org/10.1021/acsnano.6c03646).” *ACS Nano* 20, 14813–14827 (2026).

[^martini]: Yangaliev D, Ozkan SB. “[Coarse-grained RNA model for the Martini 3 force field](https://doi.org/10.1016/j.bpj.2025.07.034).” *Biophysical Journal* 125, 445–456 (2026; published online 2025), PMID [40753455](https://pubmed.ncbi.nlm.nih.gov/40753455/).

[^oxrna]: Šulc P, Ouldridge TE, Romano F, Doye JPK, Louis AA. “[Modelling toehold-mediated RNA strand displacement](https://doi.org/10.1016/j.bpj.2015.01.023).” *Biophysical Journal* 108, 1238–1247 (2015).

[^oxna_hybrid]: Ratajczyk EJ, Šulc P, Turberfield AJ, Doye JPK, Louis AA. “[Coarse-grained modeling of DNA–RNA hybrids](https://doi.org/10.1063/5.0199558).” *Journal of Chemical Physics* 160, 115101 (2024).

[^kinetics]: Todisco M, Szostak JW. “[Hybridization kinetics of out-of-equilibrium mixtures of short RNA oligonucleotides](https://doi.org/10.1093/nar/gkac784).” *Nucleic Acids Research* 50, 9647–9662 (2022).

[^tertiary]: Chauhan S, Woodson SA. “[Tertiary interactions determine the accuracy of RNA folding](https://doi.org/10.1021/ja076166i).” *Journal of the American Chemical Society* 130, 1296–1303 (2008).

[^local_context]: Lange SJ, Maticzka D, Möhl M, Gagnon JN, Brown CM, Backofen R. “[Global or local? Predicting secondary structure and accessibility in mRNAs](https://doi.org/10.1093/nar/gks181).” *Nucleic Acids Research* 40, 5215–5226 (2012).

[^probing_interaction]: Miladi M, Montaseri S, Backofen R, Raden M. “[Integration of accessibility data from structure probing into RNA–RNA interaction prediction](https://doi.org/10.1093/bioinformatics/bty1029).” *Bioinformatics* 35, 2862–2864 (2019).
