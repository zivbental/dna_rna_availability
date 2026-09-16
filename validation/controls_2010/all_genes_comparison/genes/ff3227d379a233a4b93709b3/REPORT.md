# YDR349C
Status: ok. Length: 1977 nt. Measured usable bases: 1275. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1275 | 0.2971 | 0.2710 |
| rnafold | ok | 1275 | 0.2108 | 0.1895 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 574 | -0.2749 | -0.2469 |
| seed_p | 574 | -0.3757 | -0.2255 |
| seed_p_vs_seed_pars | 419 | -0.3469 | -0.1690 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
