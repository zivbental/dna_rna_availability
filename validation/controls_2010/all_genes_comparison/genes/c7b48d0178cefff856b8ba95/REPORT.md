# YDL193W
Status: ok. Length: 1334 nt. Measured usable bases: 713. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 713 | 0.3716 | 0.3441 |
| rnafold | ok | 713 | 0.2930 | 0.2741 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 177 | 0.0019 | 0.0236 |
| seed_p | 177 | -0.1041 | -0.0628 |
| seed_p_vs_seed_pars | 97 | 0.4846 | 0.5995 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
