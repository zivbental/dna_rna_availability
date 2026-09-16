# YBL057C
Status: ok. Length: 702 nt. Measured usable bases: 454. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 454 | 0.4384 | 0.4531 |
| rnafold | ok | 454 | 0.3517 | 0.3548 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 273 | -0.0880 | -0.4207 |
| seed_p | 273 | -0.2776 | -0.3337 |
| seed_p_vs_seed_pars | 199 | -0.5293 | -0.5867 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
