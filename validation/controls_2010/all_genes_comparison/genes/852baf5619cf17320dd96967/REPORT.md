# YHR208W
Status: ok. Length: 1361 nt. Measured usable bases: 1042. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1042 | 0.3577 | 0.3393 |
| rnafold | ok | 1042 | 0.3393 | 0.3194 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 832 | -0.2902 | 0.0058 |
| seed_p | 832 | -0.2626 | -0.1500 |
| seed_p_vs_seed_pars | 725 | -0.3542 | -0.3181 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
