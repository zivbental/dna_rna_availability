# YOL133W
Status: ok. Length: 653 nt. Measured usable bases: 465. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 465 | 0.3597 | 0.3569 |
| rnafold | ok | 465 | 0.2983 | 0.3010 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 322 | -0.2434 | -0.4202 |
| seed_p | 322 | -0.1960 | -0.1262 |
| seed_p_vs_seed_pars | 230 | -0.5070 | -0.3537 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
