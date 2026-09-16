# YNR032W
Status: ok. Length: 1236 nt. Measured usable bases: 672. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 672 | 0.3225 | 0.3163 |
| rnafold | ok | 672 | 0.2255 | 0.2183 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 214 | 0.0054 | -0.0687 |
| seed_p | 214 | 0.2709 | 0.3396 |
| seed_p_vs_seed_pars | 159 | 0.0932 | 0.1433 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
