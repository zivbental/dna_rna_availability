# YFL017C
Status: ok. Length: 681 nt. Measured usable bases: 275. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 275 | 0.3042 | 0.2699 |
| rnafold | ok | 275 | 0.1425 | 0.1276 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 70 | 0.3968 | 0.2758 |
| seed_p | 70 | 0.4393 | 0.6935 |
| seed_p_vs_seed_pars | 54 | 0.4707 | 0.4886 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
