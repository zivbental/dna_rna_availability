# YLR370C
Status: ok. Length: 706 nt. Measured usable bases: 523. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 523 | 0.2373 | 0.2361 |
| rnafold | ok | 523 | 0.2430 | 0.2405 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 389 | 0.0727 | -0.1915 |
| seed_p | 389 | 0.0452 | 0.0014 |
| seed_p_vs_seed_pars | 302 | -0.1548 | -0.1646 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
