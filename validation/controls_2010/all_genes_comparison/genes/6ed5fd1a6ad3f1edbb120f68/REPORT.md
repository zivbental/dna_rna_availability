# YJR118C
Status: ok. Length: 760 nt. Measured usable bases: 372. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 372 | 0.1980 | 0.1917 |
| rnafold | ok | 372 | 0.1716 | 0.1375 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | -0.2687 | -0.3498 |
| seed_p | 135 | -0.6080 | -0.5520 |
| seed_p_vs_seed_pars | 114 | -0.3842 | -0.1920 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
