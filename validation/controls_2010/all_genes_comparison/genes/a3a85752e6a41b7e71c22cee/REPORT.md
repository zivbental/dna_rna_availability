# YBR268W
Status: ok. Length: 420 nt. Measured usable bases: 251. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 251 | 0.3376 | 0.3161 |
| rnafold | ok | 251 | 0.2863 | 0.2529 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | -0.7022 | -0.6574 |
| seed_p | 101 | -0.7252 | -0.6400 |
| seed_p_vs_seed_pars | 61 | -0.7420 | -0.6565 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
