# YCR075C
Status: ok. Length: 899 nt. Measured usable bases: 527. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 527 | 0.2649 | 0.2720 |
| rnafold | ok | 527 | 0.1829 | 0.1783 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 263 | -0.0662 | -0.0531 |
| seed_p | 263 | -0.0804 | -0.1954 |
| seed_p_vs_seed_pars | 209 | -0.0839 | -0.1498 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
