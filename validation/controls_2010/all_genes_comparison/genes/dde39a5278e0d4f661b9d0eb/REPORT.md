# YJL005W
Status: ok. Length: 6450 nt. Measured usable bases: 2110. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2110 | 0.3382 | 0.3299 |
| rnafold | ok | 2110 | 0.2685 | 0.2661 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 164 | 0.0448 | 0.3015 |
| seed_p | 164 | -0.1388 | -0.1219 |
| seed_p_vs_seed_pars | 96 | -0.4570 | -0.1723 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
