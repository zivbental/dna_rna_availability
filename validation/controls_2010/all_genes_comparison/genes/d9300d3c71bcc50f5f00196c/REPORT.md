# YBR199W
Status: ok. Length: 1599 nt. Measured usable bases: 1116. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1116 | 0.3633 | 0.3526 |
| rnafold | ok | 1116 | 0.2965 | 0.2942 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 641 | -0.1061 | -0.3312 |
| seed_p | 641 | -0.2052 | -0.2767 |
| seed_p_vs_seed_pars | 491 | -0.4212 | -0.5436 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
