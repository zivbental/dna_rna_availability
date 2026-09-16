# YGL189C
Status: ok. Length: 803 nt. Measured usable bases: 255. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 255 | 0.2753 | 0.2869 |
| rnafold | ok | 255 | 0.3239 | 0.3670 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 115 | -0.2356 | -0.5462 |
| seed_p | 115 | 0.3001 | 0.1772 |
| seed_p_vs_seed_pars | 107 | -0.0351 | -0.2898 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
