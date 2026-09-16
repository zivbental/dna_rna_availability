# YGR216C
Status: ok. Length: 1945 nt. Measured usable bases: 811. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 811 | 0.2586 | 0.2357 |
| rnafold | ok | 811 | 0.2519 | 0.2324 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 110 | -0.0706 | -0.0951 |
| seed_p | 110 | -0.0796 | -0.0912 |
| seed_p_vs_seed_pars | 54 | 0.0505 | 0.2125 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
