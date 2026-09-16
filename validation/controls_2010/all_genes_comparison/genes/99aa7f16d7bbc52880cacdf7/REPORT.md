# YER082C
Status: ok. Length: 1808 nt. Measured usable bases: 688. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 688 | 0.3065 | 0.2995 |
| rnafold | ok | 688 | 0.2334 | 0.2346 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 74 | -0.1953 | -0.3000 |
| seed_p | 74 | -0.3218 | -0.1664 |
| seed_p_vs_seed_pars | 58 | -0.4931 | -0.5086 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
