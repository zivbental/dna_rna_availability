# YBR037C
Status: ok. Length: 960 nt. Measured usable bases: 443.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 443 | 0.3696 | 0.3476 |
| rnafold | ok | 443 | 0.2501 | 0.3316 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | -0.5899 | 0.1641 |
| seed_p | 49 | -0.4901 | -0.2277 |
| seed_p_vs_seed_pars | 43 | 0.1735 | 0.1052 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
