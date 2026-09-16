# YOR294W
Status: ok. Length: 809 nt. Measured usable bases: 467. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 467 | 0.3769 | 0.3396 |
| rnafold | ok | 467 | 0.2401 | 0.2240 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 147 | 0.2119 | 0.3344 |
| seed_p | 147 | 0.0428 | -0.0960 |
| seed_p_vs_seed_pars | 127 | 0.0940 | -0.0389 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
