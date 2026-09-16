# YER011W
Status: ok. Length: 985 nt. Measured usable bases: 519. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 519 | 0.2794 | 0.2594 |
| rnafold | ok | 519 | 0.1997 | 0.1772 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 235 | -0.3146 | -0.3444 |
| seed_p | 235 | -0.5401 | -0.5040 |
| seed_p_vs_seed_pars | 180 | -0.6362 | -0.4900 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
