# YFR030W
Status: ok. Length: 3210 nt. Measured usable bases: 1213. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1213 | 0.2980 | 0.2885 |
| rnafold | ok | 1213 | 0.2875 | 0.2945 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 83 | 0.1787 | 0.2022 |
| seed_p | 83 | -0.3111 | -0.2927 |
| seed_p_vs_seed_pars | 60 | -0.2987 | -0.3931 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
