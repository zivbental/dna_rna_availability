# YOR356W
Status: ok. Length: 2095 nt. Measured usable bases: 984. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 984 | 0.4010 | 0.3919 |
| rnafold | ok | 984 | 0.2749 | 0.2830 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 157 | -0.2626 | -0.1306 |
| seed_p | 157 | -0.1512 | -0.1202 |
| seed_p_vs_seed_pars | 110 | -0.3585 | -0.2509 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
