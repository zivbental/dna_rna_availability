# YGR101W
Status: ok. Length: 1188 nt. Measured usable bases: 596. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 596 | 0.3588 | 0.3456 |
| rnafold | ok | 596 | 0.3066 | 0.2830 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 96 | -0.1030 | -0.0259 |
| seed_p | 96 | -0.4048 | -0.4841 |
| seed_p_vs_seed_pars | 79 | -0.5048 | -0.4522 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
