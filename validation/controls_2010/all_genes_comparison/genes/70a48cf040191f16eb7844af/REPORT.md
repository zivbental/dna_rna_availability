# YMR229C
Status: ok. Length: 5379 nt. Measured usable bases: 2714. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2714 | 0.3724 | 0.3564 |
| rnafold | ok | 2714 | 0.2935 | 0.2747 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 523 | -0.1490 | -0.3180 |
| seed_p | 523 | -0.3136 | -0.3258 |
| seed_p_vs_seed_pars | 363 | -0.5965 | -0.5538 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
