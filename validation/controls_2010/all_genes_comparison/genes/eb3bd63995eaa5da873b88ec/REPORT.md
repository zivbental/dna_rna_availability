# YBL033C
Status: ok. Length: 1130 nt. Measured usable bases: 581. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 581 | 0.3684 | 0.3659 |
| rnafold | ok | 581 | 0.3318 | 0.3121 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | -0.3529 | -0.3594 |
| seed_p | 72 | -0.5018 | -0.5207 |
| seed_p_vs_seed_pars | 63 | -0.6324 | -0.6082 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
