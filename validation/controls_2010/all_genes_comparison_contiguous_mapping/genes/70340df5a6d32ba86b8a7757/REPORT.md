# YBR025C
Status: ok. Length: 1408 nt. Measured usable bases: 1220.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1220 | 0.3065 | 0.3068 |
| rnafold | ok | 1220 | 0.2866 | 0.2666 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1155 | -0.1080 | -0.1220 |
| seed_p | 1155 | -0.1531 | -0.1753 |
| seed_p_vs_seed_pars | 1026 | -0.1400 | -0.1560 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
