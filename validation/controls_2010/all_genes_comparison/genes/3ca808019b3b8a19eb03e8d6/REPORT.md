# YLR005W
Status: ok. Length: 1658 nt. Measured usable bases: 741. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 741 | 0.2852 | 0.2893 |
| rnafold | ok | 741 | 0.2590 | 0.2549 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | -0.3526 | -0.3610 |
| seed_p | 72 | 0.1111 | 0.2404 |
| seed_p_vs_seed_pars | 33 | 0.7639 | 0.7321 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
