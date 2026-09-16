# YNL312W
Status: ok. Length: 928 nt. Measured usable bases: 581. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 581 | 0.3327 | 0.3152 |
| rnafold | ok | 581 | 0.2592 | 0.2652 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 312 | -0.2293 | -0.2034 |
| seed_p | 312 | -0.4145 | -0.4976 |
| seed_p_vs_seed_pars | 266 | -0.5229 | -0.5749 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
