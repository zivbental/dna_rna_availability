# YER062C
Status: ok. Length: 1098 nt. Measured usable bases: 720. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 720 | 0.3110 | 0.3001 |
| rnafold | ok | 720 | 0.2522 | 0.2404 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 394 | -0.3357 | -0.1169 |
| seed_p | 394 | -0.4081 | -0.2733 |
| seed_p_vs_seed_pars | 292 | -0.4851 | -0.3249 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
