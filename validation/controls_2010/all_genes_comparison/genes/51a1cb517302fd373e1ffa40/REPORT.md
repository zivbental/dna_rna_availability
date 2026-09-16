# YML130C
Status: ok. Length: 1830 nt. Measured usable bases: 1023. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1023 | 0.3328 | 0.3092 |
| rnafold | ok | 1023 | 0.3116 | 0.2985 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 296 | -0.1122 | -0.1401 |
| seed_p | 296 | -0.0168 | -0.0254 |
| seed_p_vs_seed_pars | 198 | -0.0765 | -0.1770 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
