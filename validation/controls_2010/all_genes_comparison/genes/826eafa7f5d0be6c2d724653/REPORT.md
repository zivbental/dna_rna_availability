# YOL143C
Status: ok. Length: 608 nt. Measured usable bases: 501. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 501 | 0.2510 | 0.2667 |
| rnafold | ok | 501 | 0.2675 | 0.2871 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 448 | -0.0218 | -0.2407 |
| seed_p | 448 | -0.0604 | -0.1884 |
| seed_p_vs_seed_pars | 402 | -0.0873 | -0.1871 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
