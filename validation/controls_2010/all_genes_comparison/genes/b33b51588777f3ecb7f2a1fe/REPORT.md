# YDL144C
Status: ok. Length: 1184 nt. Measured usable bases: 688. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 688 | 0.3755 | 0.3771 |
| rnafold | ok | 688 | 0.3648 | 0.3785 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 260 | 0.1259 | 0.0700 |
| seed_p | 260 | -0.0297 | 0.0342 |
| seed_p_vs_seed_pars | 186 | -0.2253 | -0.1695 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
