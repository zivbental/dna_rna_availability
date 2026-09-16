# YCR005C
Status: ok. Length: 1555 nt. Measured usable bases: 752. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 752 | 0.3156 | 0.3024 |
| rnafold | ok | 752 | 0.2901 | 0.2954 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | -0.0492 | -0.1991 |
| seed_p | 73 | 0.1614 | 0.0281 |
| seed_p_vs_seed_pars | 38 | 0.6207 | 0.8861 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
