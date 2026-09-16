# RDN18-2
Status: ok. Length: 1800 nt. Measured usable bases: 1766.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1766 | 0.3912 | 0.3659 |
| rnafold | ok | 1766 | 0.3619 | 0.3295 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1743 | 0.1331 | -0.0125 |
| seed_p | 1743 | 0.0045 | 0.0213 |
| seed_p_vs_seed_pars | 1732 | -0.2470 | -0.1882 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
