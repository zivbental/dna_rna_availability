# YDR370C
Status: ok. Length: 1329 nt. Measured usable bases: 546. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 546 | 0.2949 | 0.3001 |
| rnafold | ok | 546 | 0.2786 | 0.2734 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.0464 | 0.1113 |
| seed_p | 57 | -0.4574 | -0.2983 |
| seed_p_vs_seed_pars | 44 | -0.5234 | -0.2448 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
