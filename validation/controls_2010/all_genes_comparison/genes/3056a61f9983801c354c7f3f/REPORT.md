# YDL086W
Status: ok. Length: 908 nt. Measured usable bases: 637. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 637 | 0.2894 | 0.2763 |
| rnafold | ok | 637 | 0.2228 | 0.2082 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 422 | 0.0010 | -0.1312 |
| seed_p | 422 | 0.0124 | -0.0230 |
| seed_p_vs_seed_pars | 347 | -0.0360 | -0.0277 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
