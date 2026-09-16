# YIL048W
Status: ok. Length: 3912 nt. Measured usable bases: 1410. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1410 | 0.2447 | 0.2401 |
| rnafold | ok | 1410 | 0.1907 | 0.1851 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | -0.1302 | -0.2612 |
| seed_p | 54 | 0.3275 | 0.1872 |
| seed_p_vs_seed_pars | 43 | 0.0444 | 0.2984 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
