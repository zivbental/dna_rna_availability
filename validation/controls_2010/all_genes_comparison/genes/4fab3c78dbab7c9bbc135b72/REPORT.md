# YOL011W
Status: ok. Length: 2261 nt. Measured usable bases: 1163. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1163 | 0.3190 | 0.3048 |
| rnafold | ok | 1163 | 0.2272 | 0.2251 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 270 | -0.1096 | -0.1869 |
| seed_p | 270 | -0.1737 | -0.0491 |
| seed_p_vs_seed_pars | 193 | -0.3033 | -0.2513 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
