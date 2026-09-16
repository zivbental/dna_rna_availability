# YOR008C
Status: ok. Length: 1631 nt. Measured usable bases: 930. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 930 | 0.1873 | 0.1798 |
| rnafold | ok | 930 | 0.1851 | 0.1894 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 347 | 0.1177 | 0.1858 |
| seed_p | 347 | 0.0419 | 0.0679 |
| seed_p_vs_seed_pars | 251 | 0.3449 | 0.3513 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
