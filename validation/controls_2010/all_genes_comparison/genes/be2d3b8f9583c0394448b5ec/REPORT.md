# YGL195W
Status: ok. Length: 8145 nt. Measured usable bases: 4752. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 4752 | 0.2981 | 0.2771 |
| rnafold | ok | 4752 | 0.2459 | 0.2224 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1817 | -0.0148 | 0.0085 |
| seed_p | 1817 | -0.0873 | -0.0820 |
| seed_p_vs_seed_pars | 1362 | -0.2015 | -0.2009 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
