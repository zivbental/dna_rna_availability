# YHR092C
Status: ok. Length: 1921 nt. Measured usable bases: 590. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 590 | 0.2739 | 0.2501 |
| rnafold | ok | 590 | 0.1504 | 0.1291 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | -0.4569 | -0.4831 |
| seed_p | 44 | -0.0301 | -0.1466 |
| seed_p_vs_seed_pars | 22 | -0.8541 | -0.7029 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
