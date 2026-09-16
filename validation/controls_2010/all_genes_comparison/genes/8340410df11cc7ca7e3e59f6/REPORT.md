# YDR045C
Status: ok. Length: 642 nt. Measured usable bases: 325. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 325 | 0.3388 | 0.3081 |
| rnafold | ok | 325 | 0.3505 | 0.3362 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.0655 | 0.2709 |
| seed_p | 67 | -0.6332 | -0.5400 |
| seed_p_vs_seed_pars | 41 | -0.8633 | -0.7984 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
