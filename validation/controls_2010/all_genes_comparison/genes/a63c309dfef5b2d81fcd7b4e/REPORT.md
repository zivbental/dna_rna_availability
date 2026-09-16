# YJL133C-A
Status: ok. Length: 427 nt. Measured usable bases: 184. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 184 | 0.3013 | 0.3048 |
| rnafold | ok | 184 | 0.1771 | 0.1928 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.3078 | -0.5764 |
| seed_p | 58 | -0.5260 | -0.7342 |
| seed_p_vs_seed_pars | 49 | -0.5806 | -0.5341 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
