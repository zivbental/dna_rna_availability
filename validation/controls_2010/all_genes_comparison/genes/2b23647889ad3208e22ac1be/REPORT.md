# YDR375C
Status: ok. Length: 1417 nt. Measured usable bases: 661. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 661 | 0.3842 | 0.3770 |
| rnafold | ok | 661 | 0.3652 | 0.3631 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 70 | -0.1592 | 0.0535 |
| seed_p | 70 | -0.2132 | -0.2163 |
| seed_p_vs_seed_pars | 35 | -0.6112 | -0.5696 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
