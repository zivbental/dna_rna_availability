# YLR410W
Status: ok. Length: 3567 nt. Measured usable bases: 1622. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1622 | 0.3220 | 0.3059 |
| rnafold | ok | 1622 | 0.2249 | 0.2160 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 253 | -0.1799 | -0.0234 |
| seed_p | 253 | -0.1560 | -0.1375 |
| seed_p_vs_seed_pars | 186 | -0.2456 | -0.0301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
