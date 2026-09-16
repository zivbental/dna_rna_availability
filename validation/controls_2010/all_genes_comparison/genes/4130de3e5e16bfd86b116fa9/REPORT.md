# YNL100W
Status: ok. Length: 866 nt. Measured usable bases: 424. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 424 | 0.2564 | 0.2512 |
| rnafold | ok | 424 | 0.1222 | 0.1425 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 78 | 0.6340 | 0.6345 |
| seed_p | 78 | 0.5524 | 0.5409 |
| seed_p_vs_seed_pars | 53 | 0.7191 | 0.7516 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
