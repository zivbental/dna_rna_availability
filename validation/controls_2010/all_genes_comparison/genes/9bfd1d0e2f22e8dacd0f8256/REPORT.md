# YER122C
Status: ok. Length: 1686 nt. Measured usable bases: 1007. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1007 | 0.3131 | 0.3088 |
| rnafold | ok | 1007 | 0.2163 | 0.2133 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 494 | -0.2207 | -0.2991 |
| seed_p | 494 | -0.0989 | -0.1128 |
| seed_p_vs_seed_pars | 360 | -0.0523 | -0.0370 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
