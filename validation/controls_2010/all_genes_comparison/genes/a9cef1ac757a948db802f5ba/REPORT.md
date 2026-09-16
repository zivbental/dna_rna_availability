# YGR247W
Status: ok. Length: 873 nt. Measured usable bases: 383. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 383 | 0.3160 | 0.3214 |
| rnafold | ok | 383 | 0.2880 | 0.2618 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.5138 | -0.6674 |
| seed_p | 43 | -0.7344 | -0.6167 |
| seed_p_vs_seed_pars | 22 | -0.9636 | -0.9509 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
