# YOR002W
Status: ok. Length: 1754 nt. Measured usable bases: 1248. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1248 | 0.1972 | 0.1855 |
| rnafold | ok | 1248 | 0.2062 | 0.1917 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 737 | 0.0457 | -0.1202 |
| seed_p | 737 | -0.0801 | -0.0570 |
| seed_p_vs_seed_pars | 608 | -0.2029 | -0.2301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
