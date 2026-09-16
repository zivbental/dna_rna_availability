# YBR058C
Status: ok. Length: 2393 nt. Measured usable bases: 1128. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1128 | 0.3122 | 0.3055 |
| rnafold | ok | 1128 | 0.3239 | 0.3270 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 156 | 0.1517 | 0.3541 |
| seed_p | 156 | -0.0195 | 0.1340 |
| seed_p_vs_seed_pars | 121 | -0.1000 | 0.0733 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
