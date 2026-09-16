# YDL237W
Status: ok. Length: 1271 nt. Measured usable bases: 828. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 828 | 0.2663 | 0.2353 |
| rnafold | ok | 828 | 0.2867 | 0.2549 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 408 | 0.0689 | 0.2060 |
| seed_p | 408 | 0.2199 | 0.2398 |
| seed_p_vs_seed_pars | 281 | -0.0790 | -0.0680 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
