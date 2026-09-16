# YIL154C
Status: ok. Length: 1112 nt. Measured usable bases: 573. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 573 | 0.3701 | 0.3736 |
| rnafold | ok | 573 | 0.3410 | 0.3554 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 169 | -0.2212 | -0.1761 |
| seed_p | 169 | -0.2471 | -0.1976 |
| seed_p_vs_seed_pars | 109 | -0.4146 | -0.3771 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
