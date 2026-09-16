# YGL099W
Status: ok. Length: 2006 nt. Measured usable bases: 706. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 706 | 0.3592 | 0.3491 |
| rnafold | ok | 706 | 0.2929 | 0.3014 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 38 | -0.1768 | -0.4303 |
| seed_p | 38 | -0.4073 | -0.2947 |
| seed_p_vs_seed_pars | 19 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
