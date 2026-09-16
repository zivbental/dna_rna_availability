# YOR138C
Status: ok. Length: 2100 nt. Measured usable bases: 978. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 978 | 0.3882 | 0.3687 |
| rnafold | ok | 978 | 0.3165 | 0.3042 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 138 | -0.2854 | -0.2652 |
| seed_p | 138 | -0.3786 | -0.3511 |
| seed_p_vs_seed_pars | 102 | -0.4660 | -0.4292 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
