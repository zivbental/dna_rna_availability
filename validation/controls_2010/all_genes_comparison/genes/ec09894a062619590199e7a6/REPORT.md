# YDR335W
Status: ok. Length: 4118 nt. Measured usable bases: 1631. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1631 | 0.2661 | 0.2574 |
| rnafold | ok | 1631 | 0.2109 | 0.1973 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 90 | -0.0413 | -0.0382 |
| seed_p | 90 | 0.0379 | 0.0134 |
| seed_p_vs_seed_pars | 77 | -0.2297 | -0.2268 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
