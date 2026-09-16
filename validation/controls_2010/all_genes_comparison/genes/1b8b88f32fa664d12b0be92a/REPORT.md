# YBR096W
Status: ok. Length: 847 nt. Measured usable bases: 586. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 586 | 0.3624 | 0.3607 |
| rnafold | ok | 586 | 0.2887 | 0.3096 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 364 | -0.1318 | -0.3221 |
| seed_p | 364 | -0.3335 | -0.3262 |
| seed_p_vs_seed_pars | 301 | -0.5545 | -0.3902 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
