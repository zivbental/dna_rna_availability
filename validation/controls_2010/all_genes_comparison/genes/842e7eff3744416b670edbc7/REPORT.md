# YLR450W
Status: ok. Length: 3375 nt. Measured usable bases: 1594. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1594 | 0.3476 | 0.3247 |
| rnafold | ok | 1594 | 0.2825 | 0.2778 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 244 | -0.2164 | -0.0142 |
| seed_p | 244 | -0.1346 | -0.1086 |
| seed_p_vs_seed_pars | 185 | -0.2193 | -0.1301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
