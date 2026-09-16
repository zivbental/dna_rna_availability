# YJL091C
Status: ok. Length: 1623 nt. Measured usable bases: 750. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 750 | 0.3270 | 0.3071 |
| rnafold | ok | 750 | 0.2295 | 0.2300 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.2400 | -0.3911 |
| seed_p | 143 | -0.4214 | -0.2376 |
| seed_p_vs_seed_pars | 99 | -0.5849 | -0.2818 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
