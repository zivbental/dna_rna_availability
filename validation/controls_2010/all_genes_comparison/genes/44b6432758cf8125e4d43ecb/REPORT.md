# YJL143W
Status: ok. Length: 834 nt. Measured usable bases: 662. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 662 | 0.2575 | 0.2483 |
| rnafold | ok | 662 | 0.2439 | 0.2218 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 556 | -0.0694 | -0.0238 |
| seed_p | 556 | -0.1238 | -0.1377 |
| seed_p_vs_seed_pars | 475 | 0.1043 | -0.0656 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
