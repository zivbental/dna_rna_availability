# YGR040W
Status: ok. Length: 1959 nt. Measured usable bases: 791. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 791 | 0.3432 | 0.3387 |
| rnafold | ok | 791 | 0.2567 | 0.2579 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 75 | -0.0896 | -0.1608 |
| seed_p | 75 | -0.3333 | -0.4079 |
| seed_p_vs_seed_pars | 48 | -0.5538 | -0.6269 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
