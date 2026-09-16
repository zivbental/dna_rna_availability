# YJL008C
Status: ok. Length: 1861 nt. Measured usable bases: 1398. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1398 | 0.3595 | 0.3418 |
| rnafold | ok | 1398 | 0.2857 | 0.2722 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1010 | -0.1209 | -0.0471 |
| seed_p | 1010 | -0.1624 | -0.2021 |
| seed_p_vs_seed_pars | 791 | -0.2092 | -0.2472 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
