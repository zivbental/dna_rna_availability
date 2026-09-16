# YLR438C-A
Status: ok. Length: 410 nt. Measured usable bases: 197. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 197 | 0.2274 | 0.1984 |
| rnafold | ok | 197 | 0.1955 | 0.1752 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 75 | 0.2275 | -0.2731 |
| seed_p | 75 | -0.1083 | -0.1328 |
| seed_p_vs_seed_pars | 56 | -0.4341 | -0.4562 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
