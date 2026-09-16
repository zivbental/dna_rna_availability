# YKL018W
Status: ok. Length: 1162 nt. Measured usable bases: 698. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 698 | 0.3183 | 0.3147 |
| rnafold | ok | 698 | 0.2635 | 0.2675 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 271 | -0.1667 | -0.2239 |
| seed_p | 271 | -0.2064 | -0.2281 |
| seed_p_vs_seed_pars | 179 | -0.1144 | -0.1697 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
