# YLR459W
Status: ok. Length: 1263 nt. Measured usable bases: 711. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 711 | 0.2884 | 0.2929 |
| rnafold | ok | 711 | 0.2577 | 0.2683 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 230 | 0.1163 | 0.0312 |
| seed_p | 230 | -0.0812 | 0.1488 |
| seed_p_vs_seed_pars | 183 | 0.0033 | 0.1900 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
