# YJL053W
Status: ok. Length: 1275 nt. Measured usable bases: 567. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 567 | 0.3718 | 0.3532 |
| rnafold | ok | 567 | 0.2370 | 0.2455 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | -0.3480 | -0.2180 |
| seed_p | 44 | -0.1325 | -0.0344 |
| seed_p_vs_seed_pars | 27 | -0.1781 | -0.3405 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
