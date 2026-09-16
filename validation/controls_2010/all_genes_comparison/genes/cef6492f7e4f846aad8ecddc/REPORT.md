# YGR279C
Status: ok. Length: 1242 nt. Measured usable bases: 1167. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1167 | 0.3016 | 0.2957 |
| rnafold | ok | 1167 | 0.2591 | 0.2690 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1162 | -0.0687 | -0.2221 |
| seed_p | 1162 | -0.2520 | -0.3254 |
| seed_p_vs_seed_pars | 1131 | -0.2531 | -0.2979 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
