# YKR070W
Status: ok. Length: 1250 nt. Measured usable bases: 715. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 715 | 0.2911 | 0.3000 |
| rnafold | ok | 715 | 0.2096 | 0.2453 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 249 | -0.1116 | -0.0535 |
| seed_p | 249 | -0.2322 | -0.2235 |
| seed_p_vs_seed_pars | 189 | -0.1723 | -0.2169 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
