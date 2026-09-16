# YBR288C
Status: ok. Length: 1560 nt. Measured usable bases: 755. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 755 | 0.3265 | 0.3086 |
| rnafold | ok | 755 | 0.2596 | 0.2503 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | 0.0894 | -0.1959 |
| seed_p | 135 | 0.0154 | 0.0785 |
| seed_p_vs_seed_pars | 91 | -0.2497 | -0.3042 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
