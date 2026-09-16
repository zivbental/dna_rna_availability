# YDR353W
Status: ok. Length: 1067 nt. Measured usable bases: 971. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 971 | 0.3285 | 0.3050 |
| rnafold | ok | 971 | 0.1988 | 0.1972 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 979 | -0.2061 | -0.2443 |
| seed_p | 979 | -0.2887 | -0.2789 |
| seed_p_vs_seed_pars | 893 | -0.1567 | -0.1941 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
