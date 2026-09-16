# YPL274W
Status: ok. Length: 1871 nt. Measured usable bases: 1013. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1013 | 0.3082 | 0.2916 |
| rnafold | ok | 1013 | 0.2085 | 0.1986 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 324 | -0.2487 | -0.0345 |
| seed_p | 324 | -0.2081 | -0.1973 |
| seed_p_vs_seed_pars | 248 | -0.2466 | -0.2706 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
