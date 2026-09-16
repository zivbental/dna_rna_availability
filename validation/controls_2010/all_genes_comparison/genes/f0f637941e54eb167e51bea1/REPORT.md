# YJL145W
Status: ok. Length: 991 nt. Measured usable bases: 597. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 597 | 0.3800 | 0.3639 |
| rnafold | ok | 597 | 0.2788 | 0.3072 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 280 | -0.1749 | -0.1732 |
| seed_p | 280 | -0.1391 | -0.2172 |
| seed_p_vs_seed_pars | 197 | -0.2375 | -0.2449 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
