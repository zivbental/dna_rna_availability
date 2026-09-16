# YPL099C
Status: ok. Length: 682 nt. Measured usable bases: 238. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 238 | 0.3163 | 0.3216 |
| rnafold | ok | 238 | 0.2948 | 0.2864 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 33 | 0.6210 | 0.8872 |
| seed_p | 33 | 0.1671 | 0.5001 |
| seed_p_vs_seed_pars | 33 | -0.3692 | -0.1391 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
