# YMR038C
Status: ok. Length: 882 nt. Measured usable bases: 666. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 666 | 0.3912 | 0.3812 |
| rnafold | ok | 666 | 0.3579 | 0.3545 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 525 | -0.0777 | -0.2303 |
| seed_p | 525 | -0.2840 | -0.2968 |
| seed_p_vs_seed_pars | 390 | -0.3259 | -0.3110 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
