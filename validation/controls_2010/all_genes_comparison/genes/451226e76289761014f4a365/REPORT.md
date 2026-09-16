# YLR224W
Status: ok. Length: 1329 nt. Measured usable bases: 699. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 699 | 0.3053 | 0.2957 |
| rnafold | ok | 699 | 0.2864 | 0.2955 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 162 | -0.3048 | -0.4221 |
| seed_p | 162 | -0.3979 | -0.3810 |
| seed_p_vs_seed_pars | 99 | -0.4997 | -0.5645 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
