# YOR323C
Status: ok. Length: 1434 nt. Measured usable bases: 1057. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1057 | 0.3316 | 0.3191 |
| rnafold | ok | 1057 | 0.3061 | 0.2909 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 678 | 0.1159 | 0.0018 |
| seed_p | 678 | 0.0071 | -0.1145 |
| seed_p_vs_seed_pars | 574 | -0.1136 | -0.2228 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
