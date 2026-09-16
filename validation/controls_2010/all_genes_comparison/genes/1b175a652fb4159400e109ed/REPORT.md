# YOR315W
Status: ok. Length: 1341 nt. Measured usable bases: 558. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 558 | 0.2262 | 0.2232 |
| rnafold | ok | 558 | 0.2607 | 0.2609 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 41 | -0.0349 | -0.2734 |
| seed_p | 41 | -0.3732 | -0.5800 |
| seed_p_vs_seed_pars | 15 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
