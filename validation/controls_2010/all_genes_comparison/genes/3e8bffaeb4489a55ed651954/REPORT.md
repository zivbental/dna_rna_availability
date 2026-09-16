# YMR022W
Status: ok. Length: 618 nt. Measured usable bases: 394. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 394 | 0.3167 | 0.3369 |
| rnafold | ok | 394 | 0.3037 | 0.3296 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 176 | 0.2973 | 0.3053 |
| seed_p | 176 | 0.2625 | 0.3195 |
| seed_p_vs_seed_pars | 130 | 0.2736 | 0.2855 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
