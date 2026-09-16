# YEL024W
Status: ok. Length: 1232 nt. Measured usable bases: 666. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 666 | 0.3199 | 0.3155 |
| rnafold | ok | 666 | 0.2190 | 0.2425 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 297 | -0.1489 | -0.0731 |
| seed_p | 297 | -0.2949 | -0.2224 |
| seed_p_vs_seed_pars | 213 | -0.2493 | -0.2937 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
