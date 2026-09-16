# YJL012C
Status: ok. Length: 2246 nt. Measured usable bases: 1907. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1907 | 0.3249 | 0.3096 |
| rnafold | ok | 1907 | 0.2207 | 0.1912 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1728 | 0.0208 | -0.1337 |
| seed_p | 1728 | -0.1780 | -0.1216 |
| seed_p_vs_seed_pars | 1491 | -0.3605 | -0.2799 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
