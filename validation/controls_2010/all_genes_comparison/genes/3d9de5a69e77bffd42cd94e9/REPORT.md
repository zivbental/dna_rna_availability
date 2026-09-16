# YDR050C
Status: ok. Length: 834 nt. Measured usable bases: 792. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 792 | 0.3580 | 0.3411 |
| rnafold | ok | 792 | 0.3464 | 0.3196 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 772 | -0.2602 | -0.2488 |
| seed_p | 772 | -0.3211 | -0.1169 |
| seed_p_vs_seed_pars | 766 | -0.3660 | -0.2735 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
