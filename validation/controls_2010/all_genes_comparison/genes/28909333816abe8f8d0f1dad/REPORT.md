# YCL017C
Status: ok. Length: 1713 nt. Measured usable bases: 1138. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1138 | 0.2909 | 0.2812 |
| rnafold | ok | 1138 | 0.2035 | 0.1940 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 586 | -0.2137 | -0.1567 |
| seed_p | 586 | -0.1849 | -0.1734 |
| seed_p_vs_seed_pars | 416 | -0.2883 | -0.2919 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
