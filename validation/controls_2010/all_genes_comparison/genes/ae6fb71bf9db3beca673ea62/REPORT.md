# YOR025W
Status: ok. Length: 1536 nt. Measured usable bases: 647. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 647 | 0.3678 | 0.3629 |
| rnafold | ok | 647 | 0.2066 | 0.2244 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | -0.4178 | -0.4009 |
| seed_p | 71 | -0.5957 | -0.3850 |
| seed_p_vs_seed_pars | 48 | -0.8550 | -0.8490 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
