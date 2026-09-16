# YKL104C
Status: ok. Length: 2549 nt. Measured usable bases: 1742. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1742 | 0.3190 | 0.3254 |
| rnafold | ok | 1742 | 0.2764 | 0.2790 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 991 | 0.0825 | -0.0540 |
| seed_p | 991 | 0.0179 | -0.0190 |
| seed_p_vs_seed_pars | 772 | 0.0004 | -0.0519 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
