# YHR005C
Status: ok. Length: 1583 nt. Measured usable bases: 772. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 772 | 0.3334 | 0.3296 |
| rnafold | ok | 772 | 0.2662 | 0.2608 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 167 | 0.2984 | 0.2086 |
| seed_p | 167 | 0.1751 | 0.0818 |
| seed_p_vs_seed_pars | 109 | 0.1486 | 0.0738 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
