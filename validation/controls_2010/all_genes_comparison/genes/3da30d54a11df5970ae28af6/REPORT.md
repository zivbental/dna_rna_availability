# YHL003C
Status: ok. Length: 1567 nt. Measured usable bases: 1153. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1153 | 0.3781 | 0.3612 |
| rnafold | ok | 1153 | 0.3149 | 0.3155 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 870 | -0.0858 | -0.1536 |
| seed_p | 870 | -0.1641 | -0.1258 |
| seed_p_vs_seed_pars | 701 | -0.1910 | -0.1870 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
