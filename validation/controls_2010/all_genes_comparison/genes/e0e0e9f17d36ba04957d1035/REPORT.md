# YOR301W
Status: ok. Length: 1599 nt. Measured usable bases: 1010. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1010 | 0.2961 | 0.2965 |
| rnafold | ok | 1010 | 0.2475 | 0.2581 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 446 | -0.0880 | -0.1676 |
| seed_p | 446 | -0.2267 | -0.1889 |
| seed_p_vs_seed_pars | 323 | -0.2346 | -0.2155 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
