# YDL053C
Status: ok. Length: 898 nt. Measured usable bases: 349. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 349 | 0.2775 | 0.2528 |
| rnafold | ok | 349 | 0.1666 | 0.1652 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 93 | -0.0314 | 0.2117 |
| seed_p | 93 | -0.5805 | -0.5324 |
| seed_p_vs_seed_pars | 89 | -0.5745 | -0.7032 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
