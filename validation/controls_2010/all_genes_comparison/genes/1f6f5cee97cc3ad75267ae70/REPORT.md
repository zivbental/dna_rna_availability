# YMR112C
Status: ok. Length: 841 nt. Measured usable bases: 258. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 258 | 0.3395 | 0.3255 |
| rnafold | ok | 258 | 0.2968 | 0.2806 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | -0.6049 | -0.6720 |
| seed_p | 40 | -0.6944 | -0.7766 |
| seed_p_vs_seed_pars | 35 | -0.1613 | 0.0587 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
