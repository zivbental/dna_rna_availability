# YMR319C
Status: ok. Length: 2043 nt. Measured usable bases: 857. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 857 | 0.3084 | 0.2792 |
| rnafold | ok | 857 | 0.2566 | 0.2180 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 96 | 0.3872 | 0.4518 |
| seed_p | 96 | 0.5129 | 0.5043 |
| seed_p_vs_seed_pars | 81 | -0.0547 | -0.1764 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
