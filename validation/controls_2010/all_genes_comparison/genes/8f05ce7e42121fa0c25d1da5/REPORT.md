# YDL116W
Status: ok. Length: 2289 nt. Measured usable bases: 1007. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1007 | 0.2502 | 0.2388 |
| rnafold | ok | 1007 | 0.1819 | 0.1823 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 111 | -0.1004 | -0.3287 |
| seed_p | 111 | -0.1512 | -0.1635 |
| seed_p_vs_seed_pars | 88 | -0.2924 | -0.4038 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
