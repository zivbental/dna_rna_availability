# YOR001W
Status: ok. Length: 2302 nt. Measured usable bases: 1031. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1031 | 0.4208 | 0.4036 |
| rnafold | ok | 1031 | 0.3441 | 0.3311 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 169 | -0.4248 | -0.3117 |
| seed_p | 169 | -0.4952 | -0.4417 |
| seed_p_vs_seed_pars | 126 | -0.4688 | -0.3920 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
