# YHL033C
Status: ok. Length: 1248 nt. Measured usable bases: 668. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 668 | 0.2680 | 0.2751 |
| rnafold | ok | 668 | 0.2624 | 0.2519 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 354 | -0.2619 | -0.3060 |
| seed_p | 354 | -0.3741 | -0.3686 |
| seed_p_vs_seed_pars | 292 | -0.4279 | -0.5300 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
