# YKR028W
Status: ok. Length: 3428 nt. Measured usable bases: 1337. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1337 | 0.3459 | 0.3315 |
| rnafold | ok | 1337 | 0.3082 | 0.2911 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 112 | 0.1919 | -0.2671 |
| seed_p | 112 | -0.0275 | -0.0092 |
| seed_p_vs_seed_pars | 77 | 0.2569 | 0.1543 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
