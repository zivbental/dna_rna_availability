# YGR181W
Status: ok. Length: 550 nt. Measured usable bases: 373. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 373 | 0.3300 | 0.3254 |
| rnafold | ok | 373 | 0.3070 | 0.3449 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 272 | -0.3044 | -0.4652 |
| seed_p | 272 | -0.3993 | -0.4119 |
| seed_p_vs_seed_pars | 232 | -0.5142 | -0.5627 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
