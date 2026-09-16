# YAR015W
Status: ok. Length: 1052 nt. Measured usable bases: 776. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 776 | 0.3357 | 0.3267 |
| rnafold | ok | 776 | 0.2908 | 0.2797 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 480 | -0.0123 | 0.0552 |
| seed_p | 480 | -0.1911 | -0.1302 |
| seed_p_vs_seed_pars | 328 | -0.3150 | -0.4506 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
