# YML086C
Status: ok. Length: 2055 nt. Measured usable bases: 1312. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1312 | 0.3060 | 0.2995 |
| rnafold | ok | 1312 | 0.2280 | 0.2358 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 819 | 0.0252 | -0.1465 |
| seed_p | 819 | -0.1859 | -0.1477 |
| seed_p_vs_seed_pars | 650 | -0.2673 | -0.1889 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
