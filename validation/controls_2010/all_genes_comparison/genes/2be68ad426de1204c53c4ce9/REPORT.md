# YMR105C
Status: ok. Length: 1896 nt. Measured usable bases: 804. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 804 | 0.3539 | 0.3352 |
| rnafold | ok | 804 | 0.3339 | 0.3116 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | -0.4858 | -0.4627 |
| seed_p | 61 | -0.1856 | -0.2525 |
| seed_p_vs_seed_pars | 42 | -0.4491 | -0.4242 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
