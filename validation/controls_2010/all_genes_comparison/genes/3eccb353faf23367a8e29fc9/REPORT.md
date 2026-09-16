# YDR086C
Status: ok. Length: 522 nt. Measured usable bases: 382. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 382 | 0.2211 | 0.2340 |
| rnafold | ok | 382 | 0.1589 | 0.1967 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 252 | -0.1063 | -0.0755 |
| seed_p | 252 | -0.1852 | -0.0950 |
| seed_p_vs_seed_pars | 207 | -0.2075 | -0.0796 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
