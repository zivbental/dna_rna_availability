# YER183C
Status: ok. Length: 708 nt. Measured usable bases: 425. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 425 | 0.2886 | 0.2833 |
| rnafold | ok | 425 | 0.3054 | 0.2930 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 193 | -0.0353 | -0.1546 |
| seed_p | 193 | -0.0040 | 0.0563 |
| seed_p_vs_seed_pars | 139 | -0.2073 | -0.2765 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
