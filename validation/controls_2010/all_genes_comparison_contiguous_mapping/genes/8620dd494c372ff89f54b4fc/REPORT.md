# YBR068C
Status: ok. Length: 2082 nt. Measured usable bases: 1502.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1502 | 0.2964 | 0.2833 |
| rnafold | ok | 1502 | 0.2272 | 0.2185 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 969 | -0.0035 | -0.0391 |
| seed_p | 969 | -0.1934 | -0.1693 |
| seed_p_vs_seed_pars | 766 | -0.3747 | -0.3188 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
