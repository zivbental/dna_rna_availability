# YJL002C
Status: ok. Length: 1552 nt. Measured usable bases: 1310. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1310 | 0.3137 | 0.2951 |
| rnafold | ok | 1310 | 0.2586 | 0.2591 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1216 | -0.1254 | -0.1940 |
| seed_p | 1216 | -0.2512 | -0.2848 |
| seed_p_vs_seed_pars | 1061 | -0.3402 | -0.3552 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
