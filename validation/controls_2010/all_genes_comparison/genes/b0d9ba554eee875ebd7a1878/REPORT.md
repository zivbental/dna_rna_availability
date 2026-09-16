# YLR150W
Status: ok. Length: 1052 nt. Measured usable bases: 971. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 971 | 0.4021 | 0.3994 |
| rnafold | ok | 971 | 0.3322 | 0.3286 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 962 | 0.0495 | -0.2443 |
| seed_p | 962 | -0.2670 | -0.3334 |
| seed_p_vs_seed_pars | 948 | -0.2606 | -0.3277 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
