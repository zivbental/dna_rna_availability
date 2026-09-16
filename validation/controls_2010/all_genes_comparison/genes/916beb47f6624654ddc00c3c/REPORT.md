# YER086W
Status: ok. Length: 1935 nt. Measured usable bases: 1602. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1602 | 0.2689 | 0.2403 |
| rnafold | ok | 1602 | 0.2544 | 0.2297 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1428 | -0.0300 | -0.0494 |
| seed_p | 1428 | -0.0101 | -0.0715 |
| seed_p_vs_seed_pars | 1203 | -0.0801 | -0.1111 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
