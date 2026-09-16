# YPL203W
Status: ok. Length: 1548 nt. Measured usable bases: 669. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 669 | 0.2965 | 0.2976 |
| rnafold | ok | 669 | 0.2161 | 0.2400 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 29 | 0.7789 | 0.6751 |
| seed_p | 29 | -0.4964 | -0.2527 |
| seed_p_vs_seed_pars | 21 | -0.6278 | -0.4134 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
