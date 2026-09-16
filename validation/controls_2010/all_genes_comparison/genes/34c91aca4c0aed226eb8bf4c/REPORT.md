# YDR380W
Status: ok. Length: 2177 nt. Measured usable bases: 1036. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1036 | 0.3118 | 0.3092 |
| rnafold | ok | 1036 | 0.2530 | 0.2540 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 161 | -0.3260 | -0.2243 |
| seed_p | 161 | -0.1573 | -0.0614 |
| seed_p_vs_seed_pars | 95 | -0.2935 | -0.1721 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
