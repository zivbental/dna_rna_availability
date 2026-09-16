# YCR076C
Status: ok. Length: 856 nt. Measured usable bases: 343. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 343 | 0.3772 | 0.4045 |
| rnafold | ok | 343 | 0.3307 | 0.3584 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 27 | 0.6247 | 0.5921 |
| seed_p | 27 | 0.4151 | 0.4189 |
| seed_p_vs_seed_pars | 21 | -0.8253 | -0.8792 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
