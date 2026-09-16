# YJL062W-A
Status: ok. Length: 473 nt. Measured usable bases: 307. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 307 | 0.2787 | 0.2603 |
| rnafold | ok | 307 | 0.2346 | 0.2301 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 230 | -0.0366 | -0.1651 |
| seed_p | 230 | -0.1663 | -0.2171 |
| seed_p_vs_seed_pars | 193 | -0.5321 | -0.5106 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
