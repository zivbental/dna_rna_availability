# YLR258W
Status: ok. Length: 2546 nt. Measured usable bases: 1314. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1314 | 0.3188 | 0.3039 |
| rnafold | ok | 1314 | 0.2653 | 0.2645 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 303 | -0.0921 | -0.3148 |
| seed_p | 303 | -0.1032 | -0.1848 |
| seed_p_vs_seed_pars | 245 | -0.2586 | -0.2135 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
