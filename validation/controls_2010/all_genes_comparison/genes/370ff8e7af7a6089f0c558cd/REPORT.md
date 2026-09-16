# YER119C
Status: ok. Length: 1575 nt. Measured usable bases: 726. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 726 | 0.3115 | 0.2788 |
| rnafold | ok | 726 | 0.2197 | 0.1966 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 150 | -0.0400 | -0.5898 |
| seed_p | 150 | -0.5157 | -0.6067 |
| seed_p_vs_seed_pars | 129 | -0.3283 | -0.1850 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
