# YNL161W
Status: ok. Length: 2512 nt. Measured usable bases: 993. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 993 | 0.3112 | 0.2995 |
| rnafold | ok | 993 | 0.2233 | 0.2268 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 106 | 0.3380 | 0.3712 |
| seed_p | 106 | -0.1817 | 0.0392 |
| seed_p_vs_seed_pars | 78 | -0.3193 | -0.0624 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
