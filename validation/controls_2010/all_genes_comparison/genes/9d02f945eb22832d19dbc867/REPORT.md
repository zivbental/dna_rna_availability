# YLR203C
Status: ok. Length: 1473 nt. Measured usable bases: 968. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 968 | 0.2217 | 0.2166 |
| rnafold | ok | 968 | 0.1567 | 0.1444 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 477 | -0.0188 | 0.0147 |
| seed_p | 477 | 0.1501 | 0.1758 |
| seed_p_vs_seed_pars | 352 | 0.0994 | 0.1608 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
