# YKL219W
Status: ok. Length: 1224 nt. Measured usable bases: 508. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 508 | 0.3226 | 0.3038 |
| rnafold | ok | 508 | 0.2390 | 0.2103 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | -0.1745 | -0.2562 |
| seed_p | 65 | -0.2933 | -0.1998 |
| seed_p_vs_seed_pars | 48 | -0.3555 | -0.4078 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
