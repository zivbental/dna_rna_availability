# YNL053W
Status: ok. Length: 1926 nt. Measured usable bases: 695. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 695 | 0.3301 | 0.3363 |
| rnafold | ok | 695 | 0.2184 | 0.2414 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 63 | 0.1710 | -0.2323 |
| seed_p | 63 | 0.1499 | 0.0410 |
| seed_p_vs_seed_pars | 49 | 0.1651 | 0.0942 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
