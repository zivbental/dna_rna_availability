# YHR115C
Status: ok. Length: 1503 nt. Measured usable bases: 909. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 909 | 0.2788 | 0.2644 |
| rnafold | ok | 909 | 0.2746 | 0.2644 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 364 | -0.0301 | 0.1392 |
| seed_p | 364 | -0.0482 | -0.0777 |
| seed_p_vs_seed_pars | 266 | -0.2935 | -0.3358 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
