# YKR056W
Status: ok. Length: 2228 nt. Measured usable bases: 938. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 938 | 0.3390 | 0.3347 |
| rnafold | ok | 938 | 0.2874 | 0.3001 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.3299 | -0.7236 |
| seed_p | 143 | -0.5223 | -0.5910 |
| seed_p_vs_seed_pars | 118 | -0.5393 | -0.5606 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
