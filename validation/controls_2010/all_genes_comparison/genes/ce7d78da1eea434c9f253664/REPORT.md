# YDR512C
Status: ok. Length: 598 nt. Measured usable bases: 168. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 168 | 0.2714 | 0.2708 |
| rnafold | ok | 168 | 0.2954 | 0.2623 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | 0.2198 | 0.2401 |
| seed_p | 54 | 0.3948 | 0.1463 |
| seed_p_vs_seed_pars | 36 | 0.4899 | 0.1973 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
