# YMR298W
Status: ok. Length: 592 nt. Measured usable bases: 454. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 454 | 0.2896 | 0.2857 |
| rnafold | ok | 454 | 0.2659 | 0.2872 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 334 | 0.1705 | -0.1316 |
| seed_p | 334 | -0.2091 | -0.2410 |
| seed_p_vs_seed_pars | 296 | -0.1263 | -0.1573 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
