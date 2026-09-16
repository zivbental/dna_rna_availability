# YKL183W
Status: ok. Length: 1031 nt. Measured usable bases: 612. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 612 | 0.3740 | 0.3706 |
| rnafold | ok | 612 | 0.3840 | 0.3915 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 204 | 0.0167 | 0.1340 |
| seed_p | 204 | -0.0225 | -0.0295 |
| seed_p_vs_seed_pars | 149 | 0.0879 | 0.2109 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
