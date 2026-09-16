# YJL173C
Status: ok. Length: 428 nt. Measured usable bases: 301. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 301 | 0.2949 | 0.3010 |
| rnafold | ok | 301 | 0.3109 | 0.3161 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 211 | 0.2152 | 0.0017 |
| seed_p | 211 | -0.0408 | -0.0716 |
| seed_p_vs_seed_pars | 146 | -0.1990 | -0.3231 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
