# YMR161W
Status: ok. Length: 976 nt. Measured usable bases: 497. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 497 | 0.2676 | 0.2659 |
| rnafold | ok | 497 | 0.2208 | 0.2177 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | -0.0519 | 0.0831 |
| seed_p | 92 | 0.1384 | 0.0552 |
| seed_p_vs_seed_pars | 80 | 0.0246 | 0.0820 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
