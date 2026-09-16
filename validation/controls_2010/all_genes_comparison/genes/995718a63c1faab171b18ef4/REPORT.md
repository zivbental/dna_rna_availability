# YLR099W-A
Status: ok. Length: 345 nt. Measured usable bases: 235. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 235 | 0.4234 | 0.4148 |
| rnafold | ok | 235 | 0.4265 | 0.4503 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 180 | -0.2779 | -0.5863 |
| seed_p | 180 | -0.6751 | -0.5902 |
| seed_p_vs_seed_pars | 153 | -0.7261 | -0.6675 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
