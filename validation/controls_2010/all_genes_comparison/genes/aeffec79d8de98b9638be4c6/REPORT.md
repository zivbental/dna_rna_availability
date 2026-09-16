# YOL062C
Status: ok. Length: 1731 nt. Measured usable bases: 922. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 922 | 0.2656 | 0.2632 |
| rnafold | ok | 922 | 0.2230 | 0.2195 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 351 | -0.0314 | -0.1916 |
| seed_p | 351 | 0.1642 | 0.0749 |
| seed_p_vs_seed_pars | 241 | 0.0675 | 0.0342 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
