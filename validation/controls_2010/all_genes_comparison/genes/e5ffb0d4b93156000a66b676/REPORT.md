# YPL066W
Status: ok. Length: 1599 nt. Measured usable bases: 581. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 581 | 0.2789 | 0.2387 |
| rnafold | ok | 581 | 0.2744 | 0.2551 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 35 | -0.3943 | -0.7723 |
| seed_p | 35 | -0.7308 | -0.9252 |
| seed_p_vs_seed_pars | 21 | -0.8387 | -0.8947 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
