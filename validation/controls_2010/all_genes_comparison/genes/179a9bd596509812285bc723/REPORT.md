# YPL137C
Status: ok. Length: 3911 nt. Measured usable bases: 1769. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1769 | 0.3387 | 0.3166 |
| rnafold | ok | 1769 | 0.2823 | 0.2684 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 145 | 0.0530 | -0.0033 |
| seed_p | 145 | -0.0385 | 0.0342 |
| seed_p_vs_seed_pars | 89 | -0.1104 | -0.1132 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
