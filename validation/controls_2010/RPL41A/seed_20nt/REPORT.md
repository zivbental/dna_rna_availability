# RPL41A: 20-nt targets with 8-nt seeds

Both target intervals extend the previously selected PARS-low and PARS-high 8-nt sites by six bases on each side, clamped to the original experimental comparison domain. They were not selected by scanning predicted accessibility. “Around PARS-low/high” describes the original anchor, not an experimental classification of the expanded 20-nt region.

The complete deposited transcript is folded at 37 °C with Turner 2004 and dangles=2; local window/span equal transcript length and global pairing is unrestricted. Recognition is declared as antisense_oligo. No partner sequence or interaction energy is calculated, and experimental measurements do not constrain the predictions.

The table uses global ViennaRNA constrained partition functions for both probabilities and energies (kcal/mol). Seed mode is any: all 13 possible contiguous 8-nt placements within each 20-nt target are examined, and the one with highest opening probability is reported. Best-seed P is the probability of that particular chosen segment being open; it is not the probability that at least one of the 13 segments is open.

| 20-nt target | Full-site P | Best 8-nt seed P | Seed coordinates | Full-site opening cost | Seed opening cost |
| --- | --- | --- | --- | --- | --- |
| 101–120 | 4.81902e-06 | 0.0178501 | 113–120 | 7.546 | 2.481 |
| 83–102 | 1.05482e-06 | 0.00284219 | 83–90 | 8.482 | 3.614 |


| Target label | 20-nt sequence |
| --- | --- |
| around_PARS_low_20nt | AGCGGAUUAUGAGUAAAUAA |
| around_PARS_high_20nt | GAGAGCCAGAUCCAAAUAAG |

A short seed can be exposed while much of the remaining footprint is paired. Seed P describes a possible initiation opportunity; it does not predict oligo binding, strand invasion or displacement success. PARS is a per-base assay and cannot directly validate either joint probability.

The expanded RPL41A windows overlap by two bases; they are illustrative regions, not independent replicates.

Eight adapters completed successfully; sampling uses 10,000 structures and seed 1729. Per-adapter observations and estimator scopes remain in the JSON.

[Visual report](report.html) · [JSON](report.json) · [Metrics](metrics.tsv) · [Input](target.fa)
