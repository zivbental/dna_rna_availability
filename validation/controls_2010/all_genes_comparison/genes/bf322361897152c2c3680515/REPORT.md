# YLR178C
Status: ok. Length: 792 nt. Measured usable bases: 382. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 382 | 0.2898 | 0.2779 |
| rnafold | ok | 382 | 0.2872 | 0.2875 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 117 | -0.0393 | -0.4070 |
| seed_p | 117 | -0.3369 | -0.2833 |
| seed_p_vs_seed_pars | 96 | -0.3212 | -0.3881 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
