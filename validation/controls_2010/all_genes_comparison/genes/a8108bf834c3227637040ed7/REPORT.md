# YPL271W
Status: ok. Length: 341 nt. Measured usable bases: 229. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 229 | 0.3014 | 0.2674 |
| rnafold | ok | 229 | 0.2862 | 0.2383 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.4163 | -0.6475 |
| seed_p | 143 | -0.5792 | -0.6101 |
| seed_p_vs_seed_pars | 98 | -0.5099 | -0.6473 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
