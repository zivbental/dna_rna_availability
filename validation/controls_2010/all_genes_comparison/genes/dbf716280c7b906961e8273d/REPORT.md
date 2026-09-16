# YDR037W
Status: ok. Length: 1915 nt. Measured usable bases: 1669. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1669 | 0.3219 | 0.3156 |
| rnafold | ok | 1669 | 0.2335 | 0.2403 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1566 | -0.2010 | -0.2300 |
| seed_p | 1566 | -0.3107 | -0.3462 |
| seed_p_vs_seed_pars | 1457 | -0.3364 | -0.3513 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
