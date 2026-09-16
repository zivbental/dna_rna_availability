# YMR223W
Status: ok. Length: 1899 nt. Measured usable bases: 652. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 652 | 0.3578 | 0.3506 |
| rnafold | ok | 652 | 0.2861 | 0.2589 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.5076 | -0.6656 |
| seed_p | 43 | -0.2547 | -0.3961 |
| seed_p_vs_seed_pars | 28 | 0.1955 | 0.1710 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
