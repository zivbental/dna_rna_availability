# YPL199C
Status: ok. Length: 788 nt. Measured usable bases: 392. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 392 | 0.4587 | 0.4600 |
| rnafold | ok | 392 | 0.3776 | 0.3854 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | -0.3423 | -0.4261 |
| seed_p | 77 | -0.0834 | -0.0763 |
| seed_p_vs_seed_pars | 65 | -0.2724 | -0.1597 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
