# YBL092W
Status: ok. Length: 797 nt. Measured usable bases: 539. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 539 | 0.3509 | 0.3450 |
| rnafold | ok | 539 | 0.3151 | 0.3132 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 409 | -0.2371 | -0.4442 |
| seed_p | 409 | -0.4586 | -0.5381 |
| seed_p_vs_seed_pars | 398 | -0.5568 | -0.5653 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
