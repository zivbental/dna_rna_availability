# YNR001C
Status: ok. Length: 1644 nt. Measured usable bases: 1149. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1149 | 0.3331 | 0.3267 |
| rnafold | ok | 1149 | 0.2705 | 0.2778 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 730 | 0.0048 | 0.1228 |
| seed_p | 730 | -0.1284 | -0.0437 |
| seed_p_vs_seed_pars | 504 | -0.2836 | -0.2440 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
