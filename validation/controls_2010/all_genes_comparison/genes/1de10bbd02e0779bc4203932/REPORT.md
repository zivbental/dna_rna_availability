# YGL087C
Status: ok. Length: 545 nt. Measured usable bases: 233. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 233 | 0.4163 | 0.4262 |
| rnafold | ok | 233 | 0.3616 | 0.3513 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 35 | -0.0865 | -0.5023 |
| seed_p | 35 | -0.8026 | -0.7043 |
| seed_p_vs_seed_pars | 21 | -0.9778 | -0.9141 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
