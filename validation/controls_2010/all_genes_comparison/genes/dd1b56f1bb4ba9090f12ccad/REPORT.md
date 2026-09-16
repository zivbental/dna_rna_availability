# YMR315W
Status: ok. Length: 1220 nt. Measured usable bases: 867. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 867 | 0.3422 | 0.3328 |
| rnafold | ok | 867 | 0.2807 | 0.2705 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 499 | -0.0101 | 0.0114 |
| seed_p | 499 | -0.1260 | -0.2112 |
| seed_p_vs_seed_pars | 370 | -0.0686 | -0.2305 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
