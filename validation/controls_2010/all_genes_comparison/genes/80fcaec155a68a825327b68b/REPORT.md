# YJR047C
Status: ok. Length: 604 nt. Measured usable bases: 264. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 264 | 0.2153 | 0.2035 |
| rnafold | ok | 264 | 0.2911 | 0.2639 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 48 | -0.0531 | -0.2413 |
| seed_p | 48 | -0.1185 | -0.5938 |
| seed_p_vs_seed_pars | 31 | 0.0913 | -0.4951 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
