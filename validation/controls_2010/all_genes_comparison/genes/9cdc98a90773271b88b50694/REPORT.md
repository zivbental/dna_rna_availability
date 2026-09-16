# YMR314W
Status: ok. Length: 921 nt. Measured usable bases: 743. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 743 | 0.3328 | 0.3339 |
| rnafold | ok | 743 | 0.2305 | 0.2587 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 638 | 0.0228 | -0.1564 |
| seed_p | 638 | -0.0478 | -0.0786 |
| seed_p_vs_seed_pars | 557 | -0.1135 | -0.1912 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
