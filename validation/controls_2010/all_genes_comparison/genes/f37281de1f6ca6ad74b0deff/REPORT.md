# YDR498C
Status: ok. Length: 1226 nt. Measured usable bases: 533. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 533 | 0.3433 | 0.3269 |
| rnafold | ok | 533 | 0.3071 | 0.2835 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 27 | 0.5976 | 0.5050 |
| seed_p | 27 | 0.7307 | 0.4403 |
| seed_p_vs_seed_pars | 22 | 0.8465 | 0.4253 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
