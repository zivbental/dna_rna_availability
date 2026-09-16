# YER023W
Status: ok. Length: 958 nt. Measured usable bases: 791. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 791 | 0.3143 | 0.3103 |
| rnafold | ok | 791 | 0.2560 | 0.2734 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 674 | -0.0404 | -0.1794 |
| seed_p | 674 | -0.1829 | -0.2407 |
| seed_p_vs_seed_pars | 633 | -0.3455 | -0.2548 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
