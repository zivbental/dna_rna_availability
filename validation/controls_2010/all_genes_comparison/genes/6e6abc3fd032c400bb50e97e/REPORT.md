# YJR131W
Status: ok. Length: 1706 nt. Measured usable bases: 716. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 716 | 0.3297 | 0.3036 |
| rnafold | ok | 716 | 0.2726 | 0.2532 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.0556 | 0.2192 |
| seed_p | 67 | 0.2513 | 0.2073 |
| seed_p_vs_seed_pars | 41 | -0.0847 | -0.2302 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
