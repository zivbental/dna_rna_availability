# YMR150C
Status: ok. Length: 668 nt. Measured usable bases: 326. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 326 | 0.3289 | 0.3257 |
| rnafold | ok | 326 | 0.2512 | 0.2615 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 90 | 0.2146 | -0.3134 |
| seed_p | 90 | 0.1090 | 0.0097 |
| seed_p_vs_seed_pars | 56 | -0.0510 | -0.3204 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
