# YNL116W
Status: ok. Length: 1783 nt. Measured usable bases: 670. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 670 | 0.1750 | 0.1707 |
| rnafold | ok | 670 | 0.2163 | 0.2074 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 53 | 0.2533 | 0.3963 |
| seed_p | 53 | 0.1804 | 0.0391 |
| seed_p_vs_seed_pars | 49 | 0.1110 | 0.0793 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
