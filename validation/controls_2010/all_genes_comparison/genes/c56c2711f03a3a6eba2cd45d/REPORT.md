# YLR021W
Status: ok. Length: 615 nt. Measured usable bases: 271. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 271 | 0.2236 | 0.2320 |
| rnafold | ok | 271 | 0.2836 | 0.2915 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 52 | -0.4351 | -0.4627 |
| seed_p | 52 | -0.0213 | -0.2459 |
| seed_p_vs_seed_pars | 31 | -0.4808 | -0.3715 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
