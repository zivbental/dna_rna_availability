# YLR295C
Status: ok. Length: 650 nt. Measured usable bases: 403. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 403 | 0.3410 | 0.3452 |
| rnafold | ok | 403 | 0.3046 | 0.3220 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 192 | 0.0093 | -0.2477 |
| seed_p | 192 | -0.0226 | 0.0147 |
| seed_p_vs_seed_pars | 162 | 0.2577 | 0.2568 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
