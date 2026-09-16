# YDL007W
Status: ok. Length: 1434 nt. Measured usable bases: 866. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 866 | 0.3430 | 0.3462 |
| rnafold | ok | 866 | 0.3227 | 0.3243 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 353 | -0.1596 | -0.1303 |
| seed_p | 353 | -0.2962 | -0.2871 |
| seed_p_vs_seed_pars | 255 | -0.3325 | -0.3029 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
