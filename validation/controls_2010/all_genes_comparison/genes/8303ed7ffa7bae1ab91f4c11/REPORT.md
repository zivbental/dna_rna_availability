# YLR044C
Status: ok. Length: 1778 nt. Measured usable bases: 1238. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1238 | 0.3163 | 0.2778 |
| rnafold | ok | 1238 | 0.2549 | 0.2281 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 931 | -0.0450 | -0.0968 |
| seed_p | 931 | -0.1000 | -0.0545 |
| seed_p_vs_seed_pars | 831 | -0.3341 | -0.1228 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
