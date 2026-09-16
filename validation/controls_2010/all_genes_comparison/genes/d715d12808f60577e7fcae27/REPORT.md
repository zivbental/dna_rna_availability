# YDL078C
Status: ok. Length: 1145 nt. Measured usable bases: 884. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 884 | 0.3048 | 0.3064 |
| rnafold | ok | 884 | 0.2710 | 0.2801 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 680 | -0.0027 | 0.1140 |
| seed_p | 680 | -0.0821 | -0.0590 |
| seed_p_vs_seed_pars | 570 | -0.0871 | -0.1404 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
