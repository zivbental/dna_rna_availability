# YGR128C
Status: ok. Length: 2220 nt. Measured usable bases: 1027. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1027 | 0.2407 | 0.2376 |
| rnafold | ok | 1027 | 0.1777 | 0.1835 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 90 | -0.0538 | -0.1746 |
| seed_p | 90 | -0.2875 | -0.2807 |
| seed_p_vs_seed_pars | 62 | -0.1092 | -0.3004 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
