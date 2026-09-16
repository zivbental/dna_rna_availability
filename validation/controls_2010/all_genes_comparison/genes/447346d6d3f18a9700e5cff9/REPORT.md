# YDR319C
Status: ok. Length: 1015 nt. Measured usable bases: 401. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 401 | 0.2955 | 0.2868 |
| rnafold | ok | 401 | 0.1261 | 0.1665 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 20 | -0.5437 | -0.5343 |
| seed_p | 20 | -0.2877 | -0.1015 |
| seed_p_vs_seed_pars | 11 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
