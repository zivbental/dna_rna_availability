# YIL033C
Status: ok. Length: 1454 nt. Measured usable bases: 918. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 918 | 0.3832 | 0.3724 |
| rnafold | ok | 918 | 0.3203 | 0.2937 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 401 | -0.2137 | -0.1715 |
| seed_p | 401 | -0.3720 | -0.3036 |
| seed_p_vs_seed_pars | 298 | -0.4645 | -0.3438 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
