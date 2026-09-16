# YHR144C
Status: ok. Length: 1211 nt. Measured usable bases: 444. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 444 | 0.3287 | 0.3055 |
| rnafold | ok | 444 | 0.3573 | 0.3431 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | -0.1708 | -0.6477 |
| seed_p | 67 | -0.8152 | -0.5701 |
| seed_p_vs_seed_pars | 52 | -0.8794 | -0.8649 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
