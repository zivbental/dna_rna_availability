# YLR325C
Status: ok. Length: 478 nt. Measured usable bases: 385. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 385 | 0.2835 | 0.2827 |
| rnafold | ok | 385 | 0.2941 | 0.2842 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 378 | -0.0651 | 0.1057 |
| seed_p | 378 | 0.0103 | 0.0345 |
| seed_p_vs_seed_pars | 372 | -0.1396 | -0.1769 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
