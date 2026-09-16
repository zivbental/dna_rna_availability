# YBR011C
Status: ok. Length: 965 nt. Measured usable bases: 874. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 874 | 0.3672 | 0.3569 |
| rnafold | ok | 874 | 0.2242 | 0.2247 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 847 | -0.0585 | -0.1069 |
| seed_p | 847 | -0.0947 | -0.0375 |
| seed_p_vs_seed_pars | 809 | -0.1559 | -0.0951 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
