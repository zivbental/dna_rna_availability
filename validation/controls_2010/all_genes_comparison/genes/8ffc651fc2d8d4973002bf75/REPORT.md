# YER052C
Status: ok. Length: 1754 nt. Measured usable bases: 1192. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1192 | 0.2623 | 0.2506 |
| rnafold | ok | 1192 | 0.2492 | 0.2332 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 773 | 0.0200 | -0.1166 |
| seed_p | 773 | -0.1169 | -0.1132 |
| seed_p_vs_seed_pars | 570 | -0.1238 | -0.1600 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
