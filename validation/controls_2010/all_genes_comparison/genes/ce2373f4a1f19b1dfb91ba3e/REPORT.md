# YGL186C
Status: ok. Length: 1824 nt. Measured usable bases: 1037. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1037 | 0.1752 | 0.1645 |
| rnafold | ok | 1037 | 0.1832 | 0.1800 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 355 | 0.2875 | 0.3777 |
| seed_p | 355 | 0.1102 | 0.1496 |
| seed_p_vs_seed_pars | 228 | -0.0151 | 0.0647 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
