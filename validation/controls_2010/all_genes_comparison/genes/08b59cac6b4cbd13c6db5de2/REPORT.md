# YKL019W
Status: ok. Length: 1103 nt. Measured usable bases: 734. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 734 | 0.3182 | 0.3021 |
| rnafold | ok | 734 | 0.3196 | 0.2884 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 360 | -0.0338 | 0.0578 |
| seed_p | 360 | -0.1440 | -0.0598 |
| seed_p_vs_seed_pars | 277 | -0.1196 | -0.0076 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
