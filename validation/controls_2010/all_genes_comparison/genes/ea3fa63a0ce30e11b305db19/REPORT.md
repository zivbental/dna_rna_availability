# YHR107C
Status: ok. Length: 1441 nt. Measured usable bases: 652. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 652 | 0.3319 | 0.3218 |
| rnafold | ok | 652 | 0.2870 | 0.2808 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 132 | -0.1296 | -0.3718 |
| seed_p | 132 | -0.6544 | -0.5682 |
| seed_p_vs_seed_pars | 73 | -0.5654 | -0.4628 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
