# YDR292C
Status: ok. Length: 2045 nt. Measured usable bases: 1041. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1041 | 0.3090 | 0.2992 |
| rnafold | ok | 1041 | 0.2422 | 0.2322 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 223 | -0.0928 | -0.2124 |
| seed_p | 223 | -0.5246 | -0.4917 |
| seed_p_vs_seed_pars | 163 | -0.4403 | -0.4913 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
