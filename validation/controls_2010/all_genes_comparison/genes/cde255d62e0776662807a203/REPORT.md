# YBL020W
Status: ok. Length: 1961 nt. Measured usable bases: 905. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 905 | 0.3149 | 0.3235 |
| rnafold | ok | 905 | 0.2785 | 0.2882 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | 0.0273 | 0.0564 |
| seed_p | 69 | 0.1179 | 0.2304 |
| seed_p_vs_seed_pars | 33 | -0.1086 | 0.2224 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
