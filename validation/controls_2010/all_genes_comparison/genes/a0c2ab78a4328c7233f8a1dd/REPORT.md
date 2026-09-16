# YMR002W
Status: ok. Length: 773 nt. Measured usable bases: 595. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 595 | 0.2940 | 0.2860 |
| rnafold | ok | 595 | 0.2737 | 0.2938 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 502 | -0.1412 | -0.1571 |
| seed_p | 502 | -0.1748 | -0.1338 |
| seed_p_vs_seed_pars | 416 | -0.2710 | -0.2644 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
