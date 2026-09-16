# YJL193W
Status: ok. Length: 1440 nt. Measured usable bases: 561. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 561 | 0.2237 | 0.2156 |
| rnafold | ok | 561 | 0.1849 | 0.1831 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 75 | 0.2311 | 0.2207 |
| seed_p | 75 | -0.0848 | -0.0318 |
| seed_p_vs_seed_pars | 42 | -0.0323 | 0.3039 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
