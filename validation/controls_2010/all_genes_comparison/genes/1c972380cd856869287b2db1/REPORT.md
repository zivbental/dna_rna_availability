# YKL120W
Status: ok. Length: 1249 nt. Measured usable bases: 511. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 511 | 0.2767 | 0.2526 |
| rnafold | ok | 511 | 0.2451 | 0.2343 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | -0.2006 | -0.2406 |
| seed_p | 65 | 0.0531 | 0.2298 |
| seed_p_vs_seed_pars | 41 | 0.0986 | 0.4897 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
