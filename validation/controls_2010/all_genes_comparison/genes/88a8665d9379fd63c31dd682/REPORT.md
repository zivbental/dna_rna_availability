# YIL041W
Status: ok. Length: 1091 nt. Measured usable bases: 893. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 893 | 0.4109 | 0.3945 |
| rnafold | ok | 893 | 0.3489 | 0.3397 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 860 | -0.1002 | -0.2770 |
| seed_p | 860 | -0.2679 | -0.2345 |
| seed_p_vs_seed_pars | 740 | -0.3743 | -0.3085 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
