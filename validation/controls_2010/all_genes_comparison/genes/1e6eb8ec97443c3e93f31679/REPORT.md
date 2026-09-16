# YMR083W
Status: ok. Length: 1289 nt. Measured usable bases: 1076. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1076 | 0.3150 | 0.2991 |
| rnafold | ok | 1076 | 0.2555 | 0.2431 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 962 | 0.0202 | 0.1051 |
| seed_p | 962 | 0.0654 | 0.0427 |
| seed_p_vs_seed_pars | 843 | -0.1801 | -0.1952 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
