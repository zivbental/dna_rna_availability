# YBR101C
Status: ok. Length: 922 nt. Measured usable bases: 508.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 508 | 0.2424 | 0.2428 |
| rnafold | ok | 508 | 0.1925 | 0.1869 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 129 | 0.3436 | 0.3188 |
| seed_p | 129 | 0.2600 | 0.2402 |
| seed_p_vs_seed_pars | 86 | 0.5123 | 0.4886 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
