# YNR016C
Status: ok. Length: 7327 nt. Measured usable bases: 5368. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 5368 | 0.3089 | 0.2885 |
| rnafold | ok | 5368 | 0.2593 | 0.2371 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 3629 | -0.1055 | -0.0658 |
| seed_p | 3629 | -0.1344 | -0.1071 |
| seed_p_vs_seed_pars | 2914 | -0.2809 | -0.2511 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
