# YHR069C
Status: ok. Length: 1203 nt. Measured usable bases: 789. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 789 | 0.3941 | 0.3856 |
| rnafold | ok | 789 | 0.3776 | 0.3584 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 350 | -0.0474 | 0.2425 |
| seed_p | 350 | -0.1792 | -0.1059 |
| seed_p_vs_seed_pars | 277 | -0.5118 | -0.3799 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
