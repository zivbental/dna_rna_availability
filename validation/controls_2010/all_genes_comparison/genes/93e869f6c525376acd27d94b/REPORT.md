# YMR216C
Status: ok. Length: 2603 nt. Measured usable bases: 956. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 956 | 0.2395 | 0.2460 |
| rnafold | ok | 956 | 0.1896 | 0.1858 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | -0.2201 | 0.1117 |
| seed_p | 81 | -0.0978 | -0.0201 |
| seed_p_vs_seed_pars | 44 | -0.4042 | -0.2466 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
