# YLR384C
Status: ok. Length: 4176 nt. Measured usable bases: 2008. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2008 | 0.3028 | 0.2908 |
| rnafold | ok | 2008 | 0.2511 | 0.2457 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 295 | 0.0957 | 0.2319 |
| seed_p | 295 | 0.3242 | 0.3487 |
| seed_p_vs_seed_pars | 218 | 0.0562 | 0.0270 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
