# YKL051W
Status: ok. Length: 1616 nt. Measured usable bases: 639. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 639 | 0.3335 | 0.3319 |
| rnafold | ok | 639 | 0.2983 | 0.2872 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | -0.2991 | -0.1780 |
| seed_p | 69 | -0.5725 | -0.4810 |
| seed_p_vs_seed_pars | 50 | -0.5265 | -0.4839 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
