# YER152C
Status: ok. Length: 1364 nt. Measured usable bases: 935. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 935 | 0.3154 | 0.2918 |
| rnafold | ok | 935 | 0.2404 | 0.2532 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 539 | -0.1169 | 0.1194 |
| seed_p | 539 | -0.2315 | -0.1119 |
| seed_p_vs_seed_pars | 440 | -0.2931 | -0.1827 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
