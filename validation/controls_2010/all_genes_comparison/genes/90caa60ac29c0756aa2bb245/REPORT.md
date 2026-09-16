# YJL171C
Status: ok. Length: 1408 nt. Measured usable bases: 803. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 803 | 0.2809 | 0.2489 |
| rnafold | ok | 803 | 0.1737 | 0.1369 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 340 | -0.0563 | -0.0500 |
| seed_p | 340 | -0.2444 | -0.2466 |
| seed_p_vs_seed_pars | 257 | -0.1751 | -0.1397 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
