# YNL185C
Status: ok. Length: 681 nt. Measured usable bases: 305. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 305 | 0.2691 | 0.2733 |
| rnafold | ok | 305 | 0.2266 | 0.2223 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 32 | 0.0140 | -0.1049 |
| seed_p | 32 | -0.8176 | -0.5097 |
| seed_p_vs_seed_pars | 26 | -0.9681 | -0.7802 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
