# YGL022W
Status: ok. Length: 2296 nt. Measured usable bases: 1859. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1859 | 0.2861 | 0.2842 |
| rnafold | ok | 1859 | 0.1697 | 0.1880 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1588 | 0.0590 | 0.0362 |
| seed_p | 1588 | -0.0346 | -0.0758 |
| seed_p_vs_seed_pars | 1255 | -0.0140 | -0.0789 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
