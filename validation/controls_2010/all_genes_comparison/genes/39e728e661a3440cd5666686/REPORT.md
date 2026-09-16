# YNL135C
Status: ok. Length: 562 nt. Measured usable bases: 496. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 496 | 0.2973 | 0.3028 |
| rnafold | ok | 496 | 0.2302 | 0.2577 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 477 | -0.2259 | -0.4018 |
| seed_p | 477 | -0.2596 | -0.2965 |
| seed_p_vs_seed_pars | 450 | -0.1402 | -0.1831 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
