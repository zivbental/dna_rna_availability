# YEL043W
Status: ok. Length: 2948 nt. Measured usable bases: 1199. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1199 | 0.2520 | 0.2462 |
| rnafold | ok | 1199 | 0.2438 | 0.2419 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | 0.0768 | 0.0134 |
| seed_p | 149 | 0.2528 | 0.2069 |
| seed_p_vs_seed_pars | 116 | 0.0651 | -0.0386 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
