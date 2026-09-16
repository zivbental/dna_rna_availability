# YDR212W
Status: ok. Length: 1807 nt. Measured usable bases: 1385. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1385 | 0.3335 | 0.3118 |
| rnafold | ok | 1385 | 0.2966 | 0.2780 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 961 | -0.1095 | -0.1630 |
| seed_p | 961 | -0.0533 | -0.1383 |
| seed_p_vs_seed_pars | 742 | -0.1123 | -0.2368 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
