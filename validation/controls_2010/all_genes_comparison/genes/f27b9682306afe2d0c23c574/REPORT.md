# YGR162W
Status: ok. Length: 3061 nt. Measured usable bases: 2186. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2186 | 0.3503 | 0.3521 |
| rnafold | ok | 2186 | 0.2985 | 0.2920 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1388 | 0.0501 | 0.0437 |
| seed_p | 1388 | -0.0659 | -0.0462 |
| seed_p_vs_seed_pars | 1126 | -0.2126 | -0.2043 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
