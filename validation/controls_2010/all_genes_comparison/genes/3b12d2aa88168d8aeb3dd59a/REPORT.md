# YPL211W
Status: ok. Length: 708 nt. Measured usable bases: 547. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 547 | 0.3737 | 0.3625 |
| rnafold | ok | 547 | 0.2683 | 0.2754 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 445 | -0.3393 | -0.3828 |
| seed_p | 445 | -0.3441 | -0.3890 |
| seed_p_vs_seed_pars | 377 | -0.4551 | -0.5126 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
