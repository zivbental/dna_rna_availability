# YOL092W
Status: ok. Length: 992 nt. Measured usable bases: 737. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 737 | 0.2287 | 0.2209 |
| rnafold | ok | 737 | 0.1920 | 0.1792 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 548 | -0.0406 | 0.0935 |
| seed_p | 548 | -0.2044 | -0.0984 |
| seed_p_vs_seed_pars | 425 | -0.3800 | -0.2836 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
