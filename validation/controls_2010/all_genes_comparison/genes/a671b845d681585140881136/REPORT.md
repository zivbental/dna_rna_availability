# YKR066C
Status: ok. Length: 1210 nt. Measured usable bases: 900. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 900 | 0.3180 | 0.3027 |
| rnafold | ok | 900 | 0.2770 | 0.2684 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 718 | 0.0414 | 0.0130 |
| seed_p | 718 | -0.0252 | -0.0549 |
| seed_p_vs_seed_pars | 648 | -0.2072 | -0.1589 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
