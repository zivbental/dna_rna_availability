# YNL263C
Status: ok. Length: 1193 nt. Measured usable bases: 910. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 910 | 0.2373 | 0.2308 |
| rnafold | ok | 910 | 0.1963 | 0.2010 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 715 | -0.1014 | -0.1090 |
| seed_p | 715 | -0.2782 | -0.1774 |
| seed_p_vs_seed_pars | 571 | -0.4150 | -0.2855 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
