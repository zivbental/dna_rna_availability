# YJL121C
Status: ok. Length: 882 nt. Measured usable bases: 652. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 652 | 0.2985 | 0.2762 |
| rnafold | ok | 652 | 0.2175 | 0.2172 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 600 | -0.1174 | -0.0155 |
| seed_p | 600 | -0.0210 | 0.0005 |
| seed_p_vs_seed_pars | 543 | -0.0659 | -0.1067 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
