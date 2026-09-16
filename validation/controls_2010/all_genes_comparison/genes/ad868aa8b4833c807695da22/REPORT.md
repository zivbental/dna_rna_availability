# YCL008C
Status: ok. Length: 1274 nt. Measured usable bases: 690. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 690 | 0.2597 | 0.2583 |
| rnafold | ok | 690 | 0.2066 | 0.2274 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 180 | -0.1849 | -0.4107 |
| seed_p | 180 | -0.2268 | -0.3001 |
| seed_p_vs_seed_pars | 138 | -0.2106 | -0.3514 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
