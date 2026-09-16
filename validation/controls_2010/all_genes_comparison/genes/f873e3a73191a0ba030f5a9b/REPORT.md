# YMR241W
Status: ok. Length: 1125 nt. Measured usable bases: 861. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 861 | 0.3359 | 0.3270 |
| rnafold | ok | 861 | 0.3431 | 0.3545 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 704 | 0.0263 | -0.1459 |
| seed_p | 704 | -0.1951 | -0.1437 |
| seed_p_vs_seed_pars | 610 | -0.1686 | -0.1281 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
