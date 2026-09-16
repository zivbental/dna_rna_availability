# YER134C
Status: ok. Length: 794 nt. Measured usable bases: 376. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 376 | 0.2376 | 0.2333 |
| rnafold | ok | 376 | 0.1806 | 0.1470 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 64 | -0.6037 | -0.6680 |
| seed_p | 64 | -0.1881 | -0.1903 |
| seed_p_vs_seed_pars | 55 | -0.4701 | -0.3228 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
