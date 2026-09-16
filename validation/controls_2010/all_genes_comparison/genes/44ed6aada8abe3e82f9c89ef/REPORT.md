# YBR110W
Status: ok. Length: 1451 nt. Measured usable bases: 765. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 765 | 0.2867 | 0.2754 |
| rnafold | ok | 765 | 0.1809 | 0.1586 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 114 | -0.1041 | -0.3073 |
| seed_p | 114 | -0.5164 | -0.5295 |
| seed_p_vs_seed_pars | 80 | -0.7168 | -0.6891 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
