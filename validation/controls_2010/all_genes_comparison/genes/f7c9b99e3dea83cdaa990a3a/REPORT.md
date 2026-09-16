# YKR014C
Status: ok. Length: 933 nt. Measured usable bases: 462. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 462 | 0.3567 | 0.3347 |
| rnafold | ok | 462 | 0.3125 | 0.2933 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 127 | -0.1154 | -0.1939 |
| seed_p | 127 | -0.3384 | -0.3546 |
| seed_p_vs_seed_pars | 80 | -0.3005 | -0.3780 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
