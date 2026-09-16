# YMR091C
Status: ok. Length: 1391 nt. Measured usable bases: 639. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 639 | 0.3158 | 0.3231 |
| rnafold | ok | 639 | 0.2458 | 0.2525 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 133 | 0.0856 | 0.0018 |
| seed_p | 133 | -0.1760 | -0.2286 |
| seed_p_vs_seed_pars | 107 | -0.0830 | -0.2591 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
