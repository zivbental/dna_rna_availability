# YLR264W
Status: ok. Length: 860 nt. Measured usable bases: 737. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 737 | 0.2702 | 0.2520 |
| rnafold | ok | 737 | 0.2304 | 0.2184 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 646 | -0.1115 | -0.1705 |
| seed_p | 646 | -0.2663 | -0.2319 |
| seed_p_vs_seed_pars | 603 | -0.2750 | -0.2678 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
