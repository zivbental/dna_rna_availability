# YDR158W
Status: ok. Length: 1244 nt. Measured usable bases: 1111. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1111 | 0.3107 | 0.2898 |
| rnafold | ok | 1111 | 0.3053 | 0.2846 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1114 | -0.0888 | -0.1208 |
| seed_p | 1114 | -0.2192 | -0.2031 |
| seed_p_vs_seed_pars | 1024 | -0.4295 | -0.3503 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
