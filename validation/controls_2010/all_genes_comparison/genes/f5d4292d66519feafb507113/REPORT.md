# YHR142W
Status: ok. Length: 1214 nt. Measured usable bases: 715. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 715 | 0.2404 | 0.2368 |
| rnafold | ok | 715 | 0.2638 | 0.2581 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 280 | 0.0570 | -0.0647 |
| seed_p | 280 | -0.2576 | -0.2865 |
| seed_p_vs_seed_pars | 171 | -0.3785 | -0.3561 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
