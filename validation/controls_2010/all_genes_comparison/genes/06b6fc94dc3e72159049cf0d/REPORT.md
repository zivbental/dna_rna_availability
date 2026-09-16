# YLR141W
Status: ok. Length: 1491 nt. Measured usable bases: 522. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 522 | 0.3013 | 0.2927 |
| rnafold | ok | 522 | 0.2521 | 0.2659 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.7138 | -0.6264 |
| seed_p | 39 | -0.6926 | -0.7286 |
| seed_p_vs_seed_pars | 32 | -0.9670 | -0.9465 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
