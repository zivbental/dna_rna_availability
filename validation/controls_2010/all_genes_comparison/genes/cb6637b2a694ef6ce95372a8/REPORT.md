# YPL247C
Status: ok. Length: 1725 nt. Measured usable bases: 709. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 709 | 0.3441 | 0.3366 |
| rnafold | ok | 709 | 0.2924 | 0.2847 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | 0.3892 | 0.3834 |
| seed_p | 58 | 0.1887 | 0.0643 |
| seed_p_vs_seed_pars | 14 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
