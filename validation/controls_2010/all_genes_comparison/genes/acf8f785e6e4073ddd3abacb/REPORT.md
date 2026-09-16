# YKL192C
Status: ok. Length: 522 nt. Measured usable bases: 440. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 440 | 0.2549 | 0.2210 |
| rnafold | ok | 440 | 0.1800 | 0.1721 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 431 | -0.0874 | 0.0658 |
| seed_p | 431 | 0.0011 | -0.0126 |
| seed_p_vs_seed_pars | 360 | -0.0177 | -0.0038 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
