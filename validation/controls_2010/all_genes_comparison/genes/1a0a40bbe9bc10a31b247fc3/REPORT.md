# YNR019W
Status: ok. Length: 2046 nt. Measured usable bases: 1141. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1141 | 0.3166 | 0.2906 |
| rnafold | ok | 1141 | 0.2213 | 0.2211 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 316 | -0.4752 | -0.2031 |
| seed_p | 316 | -0.4295 | -0.3093 |
| seed_p_vs_seed_pars | 230 | -0.5829 | -0.4653 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
