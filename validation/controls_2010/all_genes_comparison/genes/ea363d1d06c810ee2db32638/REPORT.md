# YFL045C
Status: ok. Length: 985 nt. Measured usable bases: 834. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 834 | 0.2221 | 0.2363 |
| rnafold | ok | 834 | 0.1733 | 0.1604 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 816 | 0.1693 | -0.0920 |
| seed_p | 816 | 0.1053 | -0.0037 |
| seed_p_vs_seed_pars | 762 | -0.0776 | -0.1143 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
