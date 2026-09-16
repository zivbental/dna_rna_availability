# YPL237W
Status: ok. Length: 967 nt. Measured usable bases: 688. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 688 | 0.3799 | 0.3548 |
| rnafold | ok | 688 | 0.3230 | 0.3043 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 448 | -0.2789 | -0.3523 |
| seed_p | 448 | -0.5446 | -0.4117 |
| seed_p_vs_seed_pars | 405 | -0.4077 | -0.3997 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
