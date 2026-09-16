# YPL030W
Status: ok. Length: 1838 nt. Measured usable bases: 811. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 811 | 0.3244 | 0.3101 |
| rnafold | ok | 811 | 0.2952 | 0.2824 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 99 | 0.1759 | 0.1751 |
| seed_p | 99 | -0.3695 | -0.4249 |
| seed_p_vs_seed_pars | 63 | -0.5434 | -0.5837 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
