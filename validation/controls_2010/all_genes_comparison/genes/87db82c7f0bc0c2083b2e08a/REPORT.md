# YLL038C
Status: ok. Length: 1016 nt. Measured usable bases: 470. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 470 | 0.3104 | 0.3371 |
| rnafold | ok | 470 | 0.2791 | 0.3088 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | 0.1552 | 0.5124 |
| seed_p | 66 | 0.5211 | 0.4933 |
| seed_p_vs_seed_pars | 51 | 0.2744 | 0.3406 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
