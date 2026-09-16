# YKL174C
Status: ok. Length: 1982 nt. Measured usable bases: 870. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 870 | 0.3434 | 0.3300 |
| rnafold | ok | 870 | 0.2967 | 0.2990 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 86 | -0.0620 | -0.3635 |
| seed_p | 86 | -0.1399 | -0.2778 |
| seed_p_vs_seed_pars | 58 | -0.3887 | -0.4088 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
