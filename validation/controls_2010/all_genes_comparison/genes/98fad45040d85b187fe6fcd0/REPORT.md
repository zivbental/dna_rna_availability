# YKR059W
Status: ok. Length: 1319 nt. Measured usable bases: 150. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 150 | 0.1390 | 0.1345 |
| rnafold | ok | 150 | 0.2938 | 0.3032 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | 0.2866 | 0.0967 |
| seed_p | 60 | 0.6232 | 0.2513 |
| seed_p_vs_seed_pars | 48 | 0.8081 | 0.4828 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
