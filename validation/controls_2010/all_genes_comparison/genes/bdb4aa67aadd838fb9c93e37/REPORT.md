# YLL029W
Status: ok. Length: 2475 nt. Measured usable bases: 1007. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1007 | 0.3140 | 0.2962 |
| rnafold | ok | 1007 | 0.2901 | 0.2907 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 129 | 0.1305 | 0.0169 |
| seed_p | 129 | -0.0731 | -0.0399 |
| seed_p_vs_seed_pars | 96 | -0.5583 | -0.2162 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
