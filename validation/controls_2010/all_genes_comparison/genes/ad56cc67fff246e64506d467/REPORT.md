# YNL015W
Status: ok. Length: 363 nt. Measured usable bases: 254. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 254 | 0.2996 | 0.3037 |
| rnafold | ok | 254 | 0.2993 | 0.3167 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 181 | -0.2491 | -0.0547 |
| seed_p | 181 | -0.3696 | -0.2056 |
| seed_p_vs_seed_pars | 154 | -0.4524 | -0.1789 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
