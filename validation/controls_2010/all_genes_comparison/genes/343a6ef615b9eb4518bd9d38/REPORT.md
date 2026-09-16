# YLR274W
Status: ok. Length: 2472 nt. Measured usable bases: 1067. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1067 | 0.2760 | 0.2660 |
| rnafold | ok | 1067 | 0.2193 | 0.2300 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 105 | -0.2321 | -0.2619 |
| seed_p | 105 | -0.3467 | -0.3053 |
| seed_p_vs_seed_pars | 59 | -0.4348 | -0.5399 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
