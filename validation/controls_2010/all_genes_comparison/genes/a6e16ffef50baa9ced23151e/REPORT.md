# YEL071W
Status: ok. Length: 1641 nt. Measured usable bases: 1251. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1251 | 0.3696 | 0.3418 |
| rnafold | ok | 1251 | 0.3389 | 0.3044 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 982 | -0.0472 | 0.0391 |
| seed_p | 982 | 0.0740 | 0.0647 |
| seed_p_vs_seed_pars | 780 | -0.1250 | 0.0200 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
