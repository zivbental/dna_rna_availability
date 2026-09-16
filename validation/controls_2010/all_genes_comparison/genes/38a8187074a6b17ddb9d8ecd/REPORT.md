# YKL004W
Status: ok. Length: 1698 nt. Measured usable bases: 1307. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1307 | 0.2360 | 0.2327 |
| rnafold | ok | 1307 | 0.1947 | 0.1836 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 965 | 0.0607 | -0.0313 |
| seed_p | 965 | -0.1057 | -0.0696 |
| seed_p_vs_seed_pars | 769 | -0.2033 | -0.1861 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
