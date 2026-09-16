# YLR046C
Status: ok. Length: 1257 nt. Measured usable bases: 515. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 515 | 0.2510 | 0.2514 |
| rnafold | ok | 515 | 0.2492 | 0.2693 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | -0.4285 | -0.0381 |
| seed_p | 79 | -0.5093 | -0.3918 |
| seed_p_vs_seed_pars | 73 | -0.5602 | -0.4544 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
