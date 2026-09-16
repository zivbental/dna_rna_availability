# YFR044C
Status: ok. Length: 1493 nt. Measured usable bases: 1277. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1277 | 0.3600 | 0.3402 |
| rnafold | ok | 1277 | 0.3127 | 0.2950 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1201 | 0.0340 | 0.0738 |
| seed_p | 1201 | -0.1748 | -0.1108 |
| seed_p_vs_seed_pars | 1047 | -0.3078 | -0.3149 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
