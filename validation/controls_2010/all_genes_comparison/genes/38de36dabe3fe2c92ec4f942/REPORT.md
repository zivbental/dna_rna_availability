# YMR099C
Status: ok. Length: 985 nt. Measured usable bases: 764. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 764 | 0.3885 | 0.3947 |
| rnafold | ok | 764 | 0.3772 | 0.3690 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 643 | -0.1864 | -0.1831 |
| seed_p | 643 | -0.4187 | -0.2496 |
| seed_p_vs_seed_pars | 553 | -0.4233 | -0.3742 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
