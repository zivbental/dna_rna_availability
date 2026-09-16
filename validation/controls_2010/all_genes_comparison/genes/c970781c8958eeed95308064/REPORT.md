# YOR322C
Status: ok. Length: 2820 nt. Measured usable bases: 1111. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1111 | 0.3590 | 0.3436 |
| rnafold | ok | 1111 | 0.2882 | 0.2624 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | 0.0462 | 0.0245 |
| seed_p | 69 | 0.2068 | 0.2073 |
| seed_p_vs_seed_pars | 49 | -0.6105 | -0.3902 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
