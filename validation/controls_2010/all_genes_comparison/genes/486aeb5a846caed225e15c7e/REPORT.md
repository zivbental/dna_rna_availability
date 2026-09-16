# YNL113W
Status: ok. Length: 601 nt. Measured usable bases: 409. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 409 | 0.3301 | 0.3361 |
| rnafold | ok | 409 | 0.3713 | 0.3766 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 267 | 0.2305 | 0.3785 |
| seed_p | 267 | 0.2554 | 0.2661 |
| seed_p_vs_seed_pars | 169 | -0.1141 | 0.0043 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
