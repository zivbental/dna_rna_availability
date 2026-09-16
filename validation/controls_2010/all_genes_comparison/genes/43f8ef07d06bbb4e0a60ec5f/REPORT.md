# YNR030W
Status: ok. Length: 1875 nt. Measured usable bases: 974. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 974 | 0.1884 | 0.1787 |
| rnafold | ok | 974 | 0.1299 | 0.1313 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 180 | -0.1620 | -0.1828 |
| seed_p | 180 | -0.1917 | -0.2256 |
| seed_p_vs_seed_pars | 128 | -0.0007 | 0.0146 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
