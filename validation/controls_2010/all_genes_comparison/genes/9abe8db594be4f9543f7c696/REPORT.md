# YBR042C
Status: ok. Length: 1285 nt. Measured usable bases: 700. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 700 | 0.3635 | 0.3648 |
| rnafold | ok | 700 | 0.3011 | 0.3303 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 234 | -0.4059 | -0.6312 |
| seed_p | 234 | -0.1118 | -0.3006 |
| seed_p_vs_seed_pars | 171 | 0.0089 | -0.3192 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
