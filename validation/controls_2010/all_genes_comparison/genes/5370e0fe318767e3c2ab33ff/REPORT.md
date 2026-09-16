# YDL224C
Status: ok. Length: 2454 nt. Measured usable bases: 1088. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1088 | 0.2266 | 0.2099 |
| rnafold | ok | 1088 | 0.1459 | 0.1459 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 147 | 0.0321 | 0.0238 |
| seed_p | 147 | -0.0793 | 0.0701 |
| seed_p_vs_seed_pars | 120 | -0.3726 | -0.0456 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
