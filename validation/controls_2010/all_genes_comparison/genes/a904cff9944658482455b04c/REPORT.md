# YCR046C
Status: ok. Length: 615 nt. Measured usable bases: 381. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 381 | 0.3671 | 0.3586 |
| rnafold | ok | 381 | 0.3287 | 0.3188 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 138 | -0.1791 | -0.3757 |
| seed_p | 138 | -0.3698 | -0.4045 |
| seed_p_vs_seed_pars | 101 | -0.2848 | -0.3639 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
