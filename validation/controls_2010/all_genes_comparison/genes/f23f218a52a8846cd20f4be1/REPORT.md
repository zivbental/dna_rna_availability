# YKR093W
Status: ok. Length: 2082 nt. Measured usable bases: 1202. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1202 | 0.2401 | 0.2252 |
| rnafold | ok | 1202 | 0.1252 | 0.1004 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 500 | 0.0496 | -0.2190 |
| seed_p | 500 | -0.0408 | -0.2064 |
| seed_p_vs_seed_pars | 395 | -0.1396 | -0.3099 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
