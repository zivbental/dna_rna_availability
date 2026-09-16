# YDR100W
Status: ok. Length: 588 nt. Measured usable bases: 389. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 389 | 0.2720 | 0.2704 |
| rnafold | ok | 389 | 0.2353 | 0.2319 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 231 | -0.0827 | -0.1676 |
| seed_p | 231 | -0.0621 | 0.0052 |
| seed_p_vs_seed_pars | 164 | -0.2350 | -0.1802 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
