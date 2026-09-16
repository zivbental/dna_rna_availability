# YDR384C
Status: ok. Length: 1058 nt. Measured usable bases: 672. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 672 | 0.2469 | 0.2421 |
| rnafold | ok | 672 | 0.1633 | 0.1730 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 403 | -0.1577 | -0.1796 |
| seed_p | 403 | -0.2019 | -0.2492 |
| seed_p_vs_seed_pars | 263 | -0.3986 | -0.3774 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
