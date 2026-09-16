# YIL157C
Status: ok. Length: 832 nt. Measured usable bases: 452. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 452 | 0.3059 | 0.2792 |
| rnafold | ok | 452 | 0.2488 | 0.2108 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 278 | 0.0072 | -0.0202 |
| seed_p | 278 | -0.0668 | -0.1358 |
| seed_p_vs_seed_pars | 200 | -0.2843 | -0.2424 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
