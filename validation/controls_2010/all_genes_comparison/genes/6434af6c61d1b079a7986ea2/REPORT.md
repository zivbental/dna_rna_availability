# YJR120W
Status: ok. Length: 351 nt. Measured usable bases: 48. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 48 | -0.0865 | -0.0572 |
| rnafold | ok | 48 | -0.0821 | -0.0591 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | -0.7772 | -0.7224 |
| seed_p | 34 | -0.6139 | -0.5954 |
| seed_p_vs_seed_pars | 15 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
