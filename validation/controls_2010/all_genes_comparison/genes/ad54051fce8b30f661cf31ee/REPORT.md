# YHR072W
Status: ok. Length: 2373 nt. Measured usable bases: 1511. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1511 | 0.2646 | 0.2587 |
| rnafold | ok | 1511 | 0.2227 | 0.2192 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 733 | 0.0039 | 0.0192 |
| seed_p | 733 | -0.1054 | -0.1147 |
| seed_p_vs_seed_pars | 587 | -0.2959 | -0.2542 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
