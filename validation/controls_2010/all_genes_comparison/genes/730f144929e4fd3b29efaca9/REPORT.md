# YLR075W
Status: ok. Length: 814 nt. Measured usable bases: 766. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 766 | 0.4205 | 0.4134 |
| rnafold | ok | 766 | 0.3475 | 0.3424 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 745 | -0.0995 | -0.0700 |
| seed_p | 745 | -0.2907 | -0.1848 |
| seed_p_vs_seed_pars | 733 | -0.3155 | -0.2360 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
