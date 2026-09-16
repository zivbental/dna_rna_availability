# YNL313C
Status: ok. Length: 2782 nt. Measured usable bases: 1192. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1192 | 0.3013 | 0.2691 |
| rnafold | ok | 1192 | 0.2495 | 0.2081 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | -0.0488 | -0.1155 |
| seed_p | 79 | -0.1302 | -0.2568 |
| seed_p_vs_seed_pars | 63 | -0.0728 | 0.0190 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
