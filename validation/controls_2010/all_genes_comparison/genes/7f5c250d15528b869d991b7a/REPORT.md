# YHR194W
Status: ok. Length: 1827 nt. Measured usable bases: 750. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 750 | 0.2832 | 0.2849 |
| rnafold | ok | 750 | 0.2371 | 0.2376 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | 0.2676 | 0.0399 |
| seed_p | 71 | -0.0094 | -0.4020 |
| seed_p_vs_seed_pars | 25 | -0.6714 | -0.7636 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
