# YMR152W
Status: ok. Length: 1243 nt. Measured usable bases: 703. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 703 | 0.3454 | 0.3389 |
| rnafold | ok | 703 | 0.2617 | 0.2352 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 218 | -0.0760 | -0.0648 |
| seed_p | 218 | -0.2542 | -0.0160 |
| seed_p_vs_seed_pars | 154 | -0.3290 | -0.1847 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
