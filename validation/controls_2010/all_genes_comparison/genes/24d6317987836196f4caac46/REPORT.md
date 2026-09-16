# YAL049C
Status: ok. Length: 890 nt. Measured usable bases: 626. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 626 | 0.3595 | 0.3399 |
| rnafold | ok | 626 | 0.3426 | 0.3261 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 367 | -0.3315 | -0.2812 |
| seed_p | 367 | -0.3299 | -0.2531 |
| seed_p_vs_seed_pars | 261 | -0.0867 | -0.0696 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
