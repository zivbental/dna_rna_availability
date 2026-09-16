# YIL093C
Status: ok. Length: 1040 nt. Measured usable bases: 448. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 448 | 0.3384 | 0.3170 |
| rnafold | ok | 448 | 0.2613 | 0.2611 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 85 | 0.0148 | 0.1449 |
| seed_p | 85 | 0.0179 | -0.0878 |
| seed_p_vs_seed_pars | 61 | 0.1399 | 0.0915 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
