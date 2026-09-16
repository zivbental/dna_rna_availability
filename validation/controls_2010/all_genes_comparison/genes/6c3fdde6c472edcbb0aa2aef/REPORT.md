# YDR107C
Status: ok. Length: 2096 nt. Measured usable bases: 752. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 752 | 0.2124 | 0.2053 |
| rnafold | ok | 752 | 0.1681 | 0.1648 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | 0.2698 | 0.0551 |
| seed_p | 71 | 0.0694 | -0.2255 |
| seed_p_vs_seed_pars | 63 | 0.0142 | -0.2142 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
