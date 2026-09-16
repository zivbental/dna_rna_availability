# YMR266W
Status: ok. Length: 3104 nt. Measured usable bases: 1724. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1724 | 0.3283 | 0.3030 |
| rnafold | ok | 1724 | 0.2642 | 0.2447 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 573 | -0.1629 | -0.0824 |
| seed_p | 573 | -0.1762 | -0.1730 |
| seed_p_vs_seed_pars | 391 | -0.1498 | -0.1661 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
