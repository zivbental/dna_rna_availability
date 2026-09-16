# YDR516C
Status: ok. Length: 1694 nt. Measured usable bases: 1057. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1057 | 0.3670 | 0.3551 |
| rnafold | ok | 1057 | 0.3103 | 0.3106 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 440 | 0.0590 | -0.0217 |
| seed_p | 440 | -0.0986 | -0.1269 |
| seed_p_vs_seed_pars | 323 | -0.1412 | -0.1408 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
