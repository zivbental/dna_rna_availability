# YGR199W
Status: ok. Length: 2280 nt. Measured usable bases: 1213. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1213 | 0.3030 | 0.2961 |
| rnafold | ok | 1213 | 0.2588 | 0.2587 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 319 | -0.0364 | -0.1427 |
| seed_p | 319 | -0.2128 | -0.1403 |
| seed_p_vs_seed_pars | 192 | -0.4062 | -0.3917 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
