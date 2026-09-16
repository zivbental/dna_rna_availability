# YAL033W
Status: ok. Length: 613 nt. Measured usable bases: 293. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 293 | 0.5076 | 0.4745 |
| rnafold | ok | 293 | 0.4024 | 0.3880 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | 0.0056 | -0.2562 |
| seed_p | 66 | -0.3233 | -0.3135 |
| seed_p_vs_seed_pars | 51 | -0.5276 | -0.1959 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
