# YNL115C
Status: ok. Length: 2103 nt. Measured usable bases: 753. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 753 | 0.3394 | 0.3211 |
| rnafold | ok | 753 | 0.3146 | 0.3222 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.2576 | -0.4055 |
| seed_p | 43 | -0.2247 | -0.3434 |
| seed_p_vs_seed_pars | 28 | -0.4353 | -0.4975 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
