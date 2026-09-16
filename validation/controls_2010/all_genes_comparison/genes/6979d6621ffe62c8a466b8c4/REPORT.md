# YKL176C
Status: ok. Length: 2870 nt. Measured usable bases: 1768. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1768 | 0.3163 | 0.2971 |
| rnafold | ok | 1768 | 0.2468 | 0.2331 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 786 | -0.0279 | -0.1408 |
| seed_p | 786 | -0.2191 | -0.2542 |
| seed_p_vs_seed_pars | 590 | -0.2828 | -0.2810 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
