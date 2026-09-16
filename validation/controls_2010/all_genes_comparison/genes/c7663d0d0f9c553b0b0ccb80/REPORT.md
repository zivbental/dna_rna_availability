# YKR084C
Status: ok. Length: 1959 nt. Measured usable bases: 942. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 942 | 0.3194 | 0.3247 |
| rnafold | ok | 942 | 0.2733 | 0.2905 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 169 | -0.2401 | -0.2283 |
| seed_p | 169 | -0.2885 | -0.2464 |
| seed_p_vs_seed_pars | 123 | -0.4836 | -0.4118 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
