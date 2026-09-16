# YDR533C
Status: ok. Length: 821 nt. Measured usable bases: 384. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 384 | 0.3920 | 0.4025 |
| rnafold | ok | 384 | 0.3499 | 0.3546 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.1052 | -0.0665 |
| seed_p | 57 | 0.0805 | -0.1724 |
| seed_p_vs_seed_pars | 53 | -0.0498 | -0.1732 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
