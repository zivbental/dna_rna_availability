# YMR035W
Status: ok. Length: 657 nt. Measured usable bases: 384. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 384 | 0.3439 | 0.3347 |
| rnafold | ok | 384 | 0.2846 | 0.2850 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | -0.1592 | -0.4940 |
| seed_p | 121 | -0.5044 | -0.5747 |
| seed_p_vs_seed_pars | 80 | -0.4963 | -0.6569 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
