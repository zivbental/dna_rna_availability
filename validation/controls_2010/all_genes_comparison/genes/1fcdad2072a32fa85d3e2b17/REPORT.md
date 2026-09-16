# YOL001W
Status: ok. Length: 1480 nt. Measured usable bases: 510. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 510 | 0.3240 | 0.3096 |
| rnafold | ok | 510 | 0.2606 | 0.2565 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 53 | 0.1328 | 0.6337 |
| seed_p | 53 | -0.6370 | -0.5187 |
| seed_p_vs_seed_pars | 45 | -0.8121 | -0.4783 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
