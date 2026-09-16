# YFR028C
Status: ok. Length: 1749 nt. Measured usable bases: 973. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 973 | 0.2674 | 0.2416 |
| rnafold | ok | 973 | 0.2430 | 0.2363 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 310 | -0.0119 | 0.0739 |
| seed_p | 310 | -0.1752 | -0.0998 |
| seed_p_vs_seed_pars | 218 | -0.3890 | -0.3194 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
