# YOR079C
Status: ok. Length: 1107 nt. Measured usable bases: 597. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 597 | 0.2900 | 0.2735 |
| rnafold | ok | 597 | 0.2089 | 0.1856 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 125 | 0.1882 | 0.1830 |
| seed_p | 125 | 0.1436 | 0.0540 |
| seed_p_vs_seed_pars | 98 | -0.2505 | -0.2694 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
