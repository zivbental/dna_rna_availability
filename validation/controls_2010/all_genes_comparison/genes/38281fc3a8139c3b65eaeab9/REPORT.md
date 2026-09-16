# YHR037W
Status: ok. Length: 1884 nt. Measured usable bases: 911. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 911 | 0.3295 | 0.3219 |
| rnafold | ok | 911 | 0.2828 | 0.2736 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 97 | -0.1147 | -0.4403 |
| seed_p | 97 | 0.0423 | -0.0986 |
| seed_p_vs_seed_pars | 54 | -0.3163 | -0.4067 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
