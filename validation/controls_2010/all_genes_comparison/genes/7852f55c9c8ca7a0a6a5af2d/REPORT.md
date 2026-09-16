# YCL030C
Status: ok. Length: 2503 nt. Measured usable bases: 1710. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1710 | 0.2887 | 0.2696 |
| rnafold | ok | 1710 | 0.2703 | 0.2625 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 946 | 0.0807 | 0.0568 |
| seed_p | 946 | -0.1021 | -0.1406 |
| seed_p_vs_seed_pars | 769 | -0.1460 | -0.1493 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
