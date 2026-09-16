# YOL038W
Status: ok. Length: 866 nt. Measured usable bases: 636. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 636 | 0.3165 | 0.3193 |
| rnafold | ok | 636 | 0.2318 | 0.2746 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 418 | -0.1659 | -0.1393 |
| seed_p | 418 | -0.1754 | -0.1656 |
| seed_p_vs_seed_pars | 334 | -0.1408 | -0.1397 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
