# YLL012W
Status: ok. Length: 1907 nt. Measured usable bases: 856. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 856 | 0.3534 | 0.3234 |
| rnafold | ok | 856 | 0.3232 | 0.3038 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 160 | -0.3991 | -0.2168 |
| seed_p | 160 | -0.1880 | -0.1799 |
| seed_p_vs_seed_pars | 119 | -0.4560 | -0.3219 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
