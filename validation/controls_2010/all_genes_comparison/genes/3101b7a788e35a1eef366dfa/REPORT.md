# YLR154C
Status: ok. Length: 450 nt. Measured usable bases: 282. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 282 | 0.2957 | 0.2985 |
| rnafold | ok | 282 | 0.3535 | 0.3491 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 125 | -0.5020 | -0.3266 |
| seed_p | 125 | -0.5786 | -0.4659 |
| seed_p_vs_seed_pars | 89 | -0.8324 | -0.7490 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
