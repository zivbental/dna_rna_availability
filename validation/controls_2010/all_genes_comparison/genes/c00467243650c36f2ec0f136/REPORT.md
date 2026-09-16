# YJR125C
Status: ok. Length: 1352 nt. Measured usable bases: 808. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 808 | 0.2905 | 0.2706 |
| rnafold | ok | 808 | 0.2833 | 0.2473 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 272 | 0.0524 | -0.0197 |
| seed_p | 272 | -0.2607 | -0.2005 |
| seed_p_vs_seed_pars | 235 | -0.4373 | -0.3277 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
