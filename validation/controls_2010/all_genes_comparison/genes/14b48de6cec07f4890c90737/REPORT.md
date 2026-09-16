# YNL282W
Status: ok. Length: 588 nt. Measured usable bases: 292. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 292 | 0.4066 | 0.3874 |
| rnafold | ok | 292 | 0.3425 | 0.3427 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | -0.5293 | -0.6206 |
| seed_p | 46 | -0.1546 | -0.2454 |
| seed_p_vs_seed_pars | 43 | -0.3697 | -0.5890 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
