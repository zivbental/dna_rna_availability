# YOL103W
Status: ok. Length: 2183 nt. Measured usable bases: 1100. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1100 | 0.3301 | 0.3269 |
| rnafold | ok | 1100 | 0.3023 | 0.3112 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 151 | -0.1929 | -0.2428 |
| seed_p | 151 | 0.0515 | -0.1202 |
| seed_p_vs_seed_pars | 94 | -0.0637 | -0.0721 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
