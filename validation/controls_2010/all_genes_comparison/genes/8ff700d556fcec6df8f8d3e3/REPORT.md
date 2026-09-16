# YHR086W
Status: ok. Length: 2108 nt. Measured usable bases: 909. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 909 | 0.3120 | 0.2755 |
| rnafold | ok | 909 | 0.1645 | 0.1395 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | -0.4517 | -0.4314 |
| seed_p | 137 | -0.4375 | -0.3847 |
| seed_p_vs_seed_pars | 107 | -0.5003 | -0.3807 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
