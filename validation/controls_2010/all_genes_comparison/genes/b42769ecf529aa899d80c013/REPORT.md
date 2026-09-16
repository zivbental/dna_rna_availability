# YDR023W
Status: ok. Length: 1568 nt. Measured usable bases: 1277. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1277 | 0.3951 | 0.3847 |
| rnafold | ok | 1277 | 0.3401 | 0.3322 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1134 | -0.0549 | -0.1747 |
| seed_p | 1134 | -0.2700 | -0.1674 |
| seed_p_vs_seed_pars | 900 | -0.4373 | -0.3716 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
