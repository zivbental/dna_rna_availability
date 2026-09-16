# YML058W
Status: ok. Length: 585 nt. Measured usable bases: 473. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 473 | 0.2840 | 0.2865 |
| rnafold | ok | 473 | 0.3076 | 0.3156 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 412 | -0.1773 | -0.3288 |
| seed_p | 412 | -0.4296 | -0.4314 |
| seed_p_vs_seed_pars | 347 | -0.3954 | -0.3522 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
