# YML113W
Status: ok. Length: 946 nt. Measured usable bases: 414. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 414 | 0.2887 | 0.2855 |
| rnafold | ok | 414 | 0.3337 | 0.3267 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | -0.2034 | 0.5828 |
| seed_p | 60 | 0.4480 | 0.5971 |
| seed_p_vs_seed_pars | 45 | -0.1124 | 0.4659 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
