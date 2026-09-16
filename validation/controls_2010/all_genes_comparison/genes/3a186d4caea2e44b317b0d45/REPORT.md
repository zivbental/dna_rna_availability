# YHR163W
Status: ok. Length: 935 nt. Measured usable bases: 755. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 755 | 0.3123 | 0.2861 |
| rnafold | ok | 755 | 0.2158 | 0.2140 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 723 | -0.1643 | -0.2208 |
| seed_p | 723 | -0.3916 | -0.2564 |
| seed_p_vs_seed_pars | 627 | -0.4999 | -0.3648 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
