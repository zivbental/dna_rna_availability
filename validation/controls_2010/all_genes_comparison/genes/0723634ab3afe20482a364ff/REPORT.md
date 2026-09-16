# YML119W
Status: ok. Length: 1249 nt. Measured usable bases: 495. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 495 | 0.2229 | 0.2331 |
| rnafold | ok | 495 | 0.2374 | 0.2439 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | -0.4715 | -0.1396 |
| seed_p | 28 | 0.1431 | 0.1783 |
| seed_p_vs_seed_pars | 22 | 0.8264 | 0.9957 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
