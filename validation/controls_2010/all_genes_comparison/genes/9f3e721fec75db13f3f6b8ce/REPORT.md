# YLR250W
Status: ok. Length: 839 nt. Measured usable bases: 548. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 548 | 0.3752 | 0.3525 |
| rnafold | ok | 548 | 0.2166 | 0.2349 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 236 | -0.0871 | -0.1132 |
| seed_p | 236 | -0.3348 | -0.3552 |
| seed_p_vs_seed_pars | 165 | -0.4362 | -0.4354 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
