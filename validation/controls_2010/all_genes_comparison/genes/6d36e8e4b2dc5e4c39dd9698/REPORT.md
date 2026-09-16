# YJR007W
Status: ok. Length: 1170 nt. Measured usable bases: 840. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 840 | 0.2285 | 0.2371 |
| rnafold | ok | 840 | 0.2014 | 0.2122 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 620 | -0.0387 | 0.0718 |
| seed_p | 620 | -0.0753 | -0.0165 |
| seed_p_vs_seed_pars | 523 | -0.0797 | -0.0577 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
