# YGL191W
Status: ok. Length: 698 nt. Measured usable bases: 445. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 445 | 0.3751 | 0.3785 |
| rnafold | ok | 445 | 0.3556 | 0.3638 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 310 | -0.2095 | -0.3157 |
| seed_p | 310 | -0.3735 | -0.5153 |
| seed_p_vs_seed_pars | 281 | -0.5026 | -0.6552 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
