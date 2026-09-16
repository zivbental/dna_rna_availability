# YOL122C
Status: ok. Length: 2013 nt. Measured usable bases: 1067. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1067 | 0.2753 | 0.2472 |
| rnafold | ok | 1067 | 0.1666 | 0.1422 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 220 | 0.0154 | -0.1064 |
| seed_p | 220 | -0.4465 | -0.4039 |
| seed_p_vs_seed_pars | 159 | -0.0559 | -0.1346 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
