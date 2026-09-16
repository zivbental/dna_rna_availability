# YJR088C
Status: ok. Length: 1015 nt. Measured usable bases: 467. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 467 | 0.3966 | 0.3979 |
| rnafold | ok | 467 | 0.3231 | 0.3378 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | 0.5276 | 0.5188 |
| seed_p | 58 | -0.2651 | -0.2523 |
| seed_p_vs_seed_pars | 48 | -0.4806 | -0.5555 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
