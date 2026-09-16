# YDL212W
Status: ok. Length: 824 nt. Measured usable bases: 689. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 689 | 0.3129 | 0.2993 |
| rnafold | ok | 689 | 0.2880 | 0.2794 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 647 | -0.0266 | -0.1426 |
| seed_p | 647 | -0.2164 | -0.1704 |
| seed_p_vs_seed_pars | 578 | -0.1112 | -0.1434 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
