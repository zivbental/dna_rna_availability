# YDR510W
Status: ok. Length: 508 nt. Measured usable bases: 391. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 391 | 0.3026 | 0.2787 |
| rnafold | ok | 391 | 0.2906 | 0.2625 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 315 | -0.0541 | 0.0685 |
| seed_p | 315 | -0.0981 | -0.1190 |
| seed_p_vs_seed_pars | 280 | -0.1851 | -0.2085 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
