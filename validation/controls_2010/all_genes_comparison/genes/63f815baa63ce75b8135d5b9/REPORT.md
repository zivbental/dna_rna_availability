# YLR175W
Status: ok. Length: 1594 nt. Measured usable bases: 1256. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1256 | 0.3482 | 0.3437 |
| rnafold | ok | 1256 | 0.3006 | 0.2952 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1092 | 0.0290 | -0.2731 |
| seed_p | 1092 | -0.2328 | -0.2587 |
| seed_p_vs_seed_pars | 913 | -0.2777 | -0.3069 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
