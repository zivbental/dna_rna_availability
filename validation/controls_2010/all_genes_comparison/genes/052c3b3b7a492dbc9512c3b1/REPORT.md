# YMR131C
Status: ok. Length: 1675 nt. Measured usable bases: 398. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 398 | 0.4091 | 0.3844 |
| rnafold | ok | 398 | 0.3998 | 0.3601 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 268 | 0.0715 | -0.1280 |
| seed_p | 268 | -0.3421 | -0.3503 |
| seed_p_vs_seed_pars | 230 | -0.5229 | -0.5306 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
