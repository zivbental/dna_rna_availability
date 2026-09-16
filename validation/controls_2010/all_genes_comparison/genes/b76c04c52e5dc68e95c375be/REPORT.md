# YOL052C
Status: ok. Length: 1351 nt. Measured usable bases: 856. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 856 | 0.2555 | 0.2462 |
| rnafold | ok | 856 | 0.1971 | 0.2021 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 363 | -0.0496 | -0.0949 |
| seed_p | 363 | -0.1150 | -0.0012 |
| seed_p_vs_seed_pars | 274 | -0.2221 | -0.2126 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
