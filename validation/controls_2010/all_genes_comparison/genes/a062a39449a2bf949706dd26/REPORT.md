# YCR084C
Status: ok. Length: 2668 nt. Measured usable bases: 1813. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1813 | 0.2529 | 0.2493 |
| rnafold | ok | 1813 | 0.1928 | 0.1930 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1088 | -0.0752 | -0.1158 |
| seed_p | 1088 | -0.0972 | -0.1033 |
| seed_p_vs_seed_pars | 862 | -0.1786 | -0.1511 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
