# YHR149C
Status: ok. Length: 2375 nt. Measured usable bases: 1041. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1041 | 0.3156 | 0.3026 |
| rnafold | ok | 1041 | 0.2836 | 0.2795 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | 0.0528 | 0.5694 |
| seed_p | 65 | 0.2331 | 0.4478 |
| seed_p_vs_seed_pars | 38 | -0.1974 | 0.5183 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
