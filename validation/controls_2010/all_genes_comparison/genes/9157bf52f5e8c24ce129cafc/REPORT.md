# YAL022C
Status: ok. Length: 1627 nt. Measured usable bases: 1209. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1209 | 0.2574 | 0.2564 |
| rnafold | ok | 1209 | 0.1823 | 0.1877 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 829 | -0.0662 | -0.0319 |
| seed_p | 829 | -0.3343 | -0.3008 |
| seed_p_vs_seed_pars | 660 | -0.4033 | -0.4515 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
