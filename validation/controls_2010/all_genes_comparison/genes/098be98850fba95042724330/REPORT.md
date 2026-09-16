# YLR414C
Status: ok. Length: 997 nt. Measured usable bases: 157. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 157 | 0.3599 | 0.3601 |
| rnafold | ok | 157 | 0.3566 | 0.3418 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | -0.4595 | -0.6814 |
| seed_p | 79 | -0.5189 | -0.5388 |
| seed_p_vs_seed_pars | 58 | -0.9135 | -0.9090 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
