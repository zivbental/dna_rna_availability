# YOR226C
Status: ok. Length: 651 nt. Measured usable bases: 329. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 329 | 0.3976 | 0.3820 |
| rnafold | ok | 329 | 0.3478 | 0.3331 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | -0.2231 | -0.1269 |
| seed_p | 118 | -0.2591 | 0.0698 |
| seed_p_vs_seed_pars | 70 | 0.1169 | 0.3026 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
