# YJL094C
Status: ok. Length: 2803 nt. Measured usable bases: 1210. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1210 | 0.2673 | 0.2456 |
| rnafold | ok | 1210 | 0.2248 | 0.1974 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 157 | -0.0727 | -0.1428 |
| seed_p | 157 | -0.2285 | -0.1594 |
| seed_p_vs_seed_pars | 104 | -0.5819 | -0.4922 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
