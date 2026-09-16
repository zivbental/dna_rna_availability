# YNR051C
Status: ok. Length: 2274 nt. Measured usable bases: 863. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 863 | 0.3780 | 0.3746 |
| rnafold | ok | 863 | 0.3024 | 0.2909 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 108 | -0.4115 | 0.0000 |
| seed_p | 108 | -0.4028 | -0.2217 |
| seed_p_vs_seed_pars | 84 | -0.2745 | -0.1560 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
