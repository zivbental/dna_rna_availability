# YGL127C
Status: ok. Length: 492 nt. Measured usable bases: 287. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 287 | 0.3688 | 0.3533 |
| rnafold | ok | 287 | 0.3407 | 0.3344 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 80 | -0.2031 | 0.5239 |
| seed_p | 80 | -0.0322 | -0.0599 |
| seed_p_vs_seed_pars | 47 | -0.2402 | -0.2331 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
