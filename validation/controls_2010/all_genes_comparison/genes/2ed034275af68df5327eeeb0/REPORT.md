# YNL207W
Status: ok. Length: 1576 nt. Measured usable bases: 872. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 872 | 0.3389 | 0.3275 |
| rnafold | ok | 872 | 0.2352 | 0.2535 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 261 | -0.1404 | -0.1838 |
| seed_p | 261 | -0.1128 | -0.1889 |
| seed_p_vs_seed_pars | 202 | -0.2055 | -0.2537 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
