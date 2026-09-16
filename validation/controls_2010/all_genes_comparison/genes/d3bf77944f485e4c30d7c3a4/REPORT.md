# YHR043C
Status: ok. Length: 894 nt. Measured usable bases: 348. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 348 | 0.2786 | 0.2850 |
| rnafold | ok | 348 | 0.1410 | 0.1434 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | -0.4562 | -0.3234 |
| seed_p | 51 | -0.3945 | -0.3410 |
| seed_p_vs_seed_pars | 45 | -0.7078 | -0.2906 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
