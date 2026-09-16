# YNL306W
Status: ok. Length: 766 nt. Measured usable bases: 422. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 422 | 0.3101 | 0.3074 |
| rnafold | ok | 422 | 0.2843 | 0.2834 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 142 | -0.1190 | -0.0190 |
| seed_p | 142 | 0.2174 | 0.2039 |
| seed_p_vs_seed_pars | 102 | 0.5706 | 0.5294 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
