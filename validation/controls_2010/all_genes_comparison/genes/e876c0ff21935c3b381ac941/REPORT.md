# YER048W-A
Status: ok. Length: 686 nt. Measured usable bases: 456. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 456 | 0.2677 | 0.2667 |
| rnafold | ok | 456 | 0.1818 | 0.1865 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 287 | 0.1472 | 0.0762 |
| seed_p | 287 | 0.0291 | -0.0073 |
| seed_p_vs_seed_pars | 251 | -0.1060 | -0.0724 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
