# YML105C
Status: ok. Length: 931 nt. Measured usable bases: 573. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 573 | 0.3431 | 0.3384 |
| rnafold | ok | 573 | 0.2923 | 0.2962 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 324 | -0.2164 | -0.1376 |
| seed_p | 324 | -0.1359 | -0.0823 |
| seed_p_vs_seed_pars | 229 | -0.3983 | -0.3410 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
