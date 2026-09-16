# YLR113W
Status: ok. Length: 1761 nt. Measured usable bases: 1304. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1304 | 0.2680 | 0.2520 |
| rnafold | ok | 1304 | 0.2074 | 0.1951 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1026 | -0.1967 | -0.0108 |
| seed_p | 1026 | -0.2520 | -0.1438 |
| seed_p_vs_seed_pars | 883 | -0.2694 | -0.2384 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
