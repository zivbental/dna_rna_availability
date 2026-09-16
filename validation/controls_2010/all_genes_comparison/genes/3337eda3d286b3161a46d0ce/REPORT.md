# YFR053C
Status: ok. Length: 1695 nt. Measured usable bases: 956. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 956 | 0.2833 | 0.2764 |
| rnafold | ok | 956 | 0.1971 | 0.2005 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 394 | 0.0181 | -0.0686 |
| seed_p | 394 | -0.2176 | -0.2571 |
| seed_p_vs_seed_pars | 306 | -0.2857 | -0.2723 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
