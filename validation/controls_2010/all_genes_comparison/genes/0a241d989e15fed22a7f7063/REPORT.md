# YOR219C
Status: ok. Length: 3206 nt. Measured usable bases: 1100. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1100 | 0.3138 | 0.2808 |
| rnafold | ok | 1100 | 0.2584 | 0.2567 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 98 | -0.4153 | -0.1703 |
| seed_p | 98 | -0.6384 | -0.5999 |
| seed_p_vs_seed_pars | 74 | -0.8021 | -0.7301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
