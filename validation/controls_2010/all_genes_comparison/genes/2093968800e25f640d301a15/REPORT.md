# YKL191W
Status: ok. Length: 1708 nt. Measured usable bases: 1233. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1233 | 0.3593 | 0.3523 |
| rnafold | ok | 1233 | 0.2730 | 0.2827 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 883 | 0.1316 | 0.0538 |
| seed_p | 883 | 0.0769 | 0.0861 |
| seed_p_vs_seed_pars | 676 | -0.0031 | 0.0197 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
