# YDR186C
Status: ok. Length: 2778 nt. Measured usable bases: 1108. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1108 | 0.2827 | 0.2544 |
| rnafold | ok | 1108 | 0.2498 | 0.2126 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 52 | -0.2084 | -0.1178 |
| seed_p | 52 | -0.3851 | -0.3225 |
| seed_p_vs_seed_pars | 36 | -0.4293 | -0.2917 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
