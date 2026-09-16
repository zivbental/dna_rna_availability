# YML021C
Status: ok. Length: 1080 nt. Measured usable bases: 527. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 527 | 0.3749 | 0.3603 |
| rnafold | ok | 527 | 0.3315 | 0.3210 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | 0.5739 | 0.4245 |
| seed_p | 58 | 0.0331 | 0.0915 |
| seed_p_vs_seed_pars | 27 | -0.0799 | 0.1556 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
