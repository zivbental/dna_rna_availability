# YOL007C
Status: ok. Length: 1428 nt. Measured usable bases: 788. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 788 | 0.2530 | 0.2688 |
| rnafold | ok | 788 | 0.2561 | 0.2610 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 247 | 0.1166 | -0.0638 |
| seed_p | 247 | 0.0103 | 0.0409 |
| seed_p_vs_seed_pars | 191 | 0.0938 | 0.1234 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
