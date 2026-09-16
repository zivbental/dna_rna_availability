# YPL212C
Status: ok. Length: 1826 nt. Measured usable bases: 826. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 826 | 0.3769 | 0.3818 |
| rnafold | ok | 826 | 0.3130 | 0.3218 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 117 | -0.1435 | 0.0447 |
| seed_p | 117 | -0.2276 | -0.1507 |
| seed_p_vs_seed_pars | 83 | -0.2196 | -0.3512 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
