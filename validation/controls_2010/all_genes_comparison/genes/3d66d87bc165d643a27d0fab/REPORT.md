# YMR250W
Status: ok. Length: 1902 nt. Measured usable bases: 748. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 748 | 0.3145 | 0.2857 |
| rnafold | ok | 748 | 0.2423 | 0.2444 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 76 | -0.4607 | 0.1318 |
| seed_p | 76 | -0.2601 | -0.2977 |
| seed_p_vs_seed_pars | 49 | -0.4628 | -0.7094 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
