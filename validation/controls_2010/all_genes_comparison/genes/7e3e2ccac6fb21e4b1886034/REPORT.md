# YOR089C
Status: ok. Length: 699 nt. Measured usable bases: 343. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 343 | 0.2387 | 0.1982 |
| rnafold | ok | 343 | 0.2078 | 0.1518 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | -0.2999 | -0.5307 |
| seed_p | 79 | -0.4632 | -0.5362 |
| seed_p_vs_seed_pars | 51 | -0.4364 | -0.5692 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
