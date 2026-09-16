# YHR045W
Status: ok. Length: 1846 nt. Measured usable bases: 945. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 945 | 0.3045 | 0.3018 |
| rnafold | ok | 945 | 0.2252 | 0.2284 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 168 | -0.3810 | -0.1327 |
| seed_p | 168 | -0.1822 | -0.1739 |
| seed_p_vs_seed_pars | 112 | -0.2649 | -0.3006 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
