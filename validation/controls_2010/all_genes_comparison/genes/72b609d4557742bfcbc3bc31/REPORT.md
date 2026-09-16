# YNR041C
Status: ok. Length: 1165 nt. Measured usable bases: 657. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 657 | 0.3404 | 0.3300 |
| rnafold | ok | 657 | 0.2646 | 0.2760 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 250 | -0.2028 | -0.3698 |
| seed_p | 250 | 0.0849 | -0.0509 |
| seed_p_vs_seed_pars | 174 | -0.3299 | -0.4789 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
