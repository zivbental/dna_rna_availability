# YGL148W
Status: ok. Length: 1265 nt. Measured usable bases: 1122. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1122 | 0.4190 | 0.4009 |
| rnafold | ok | 1122 | 0.3355 | 0.3143 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1112 | -0.2604 | -0.3362 |
| seed_p | 1112 | -0.4498 | -0.3724 |
| seed_p_vs_seed_pars | 1041 | -0.5803 | -0.4717 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
