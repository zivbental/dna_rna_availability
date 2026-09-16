# YKL065C
Status: ok. Length: 681 nt. Measured usable bases: 506. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 506 | 0.3053 | 0.3136 |
| rnafold | ok | 506 | 0.2365 | 0.2442 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 371 | -0.3762 | -0.3261 |
| seed_p | 371 | -0.2818 | -0.2502 |
| seed_p_vs_seed_pars | 322 | -0.2564 | -0.1718 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
