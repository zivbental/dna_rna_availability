# YDR190C
Status: ok. Length: 1479 nt. Measured usable bases: 954. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 954 | 0.3352 | 0.3162 |
| rnafold | ok | 954 | 0.3216 | 0.2970 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 464 | -0.0711 | -0.1587 |
| seed_p | 464 | -0.0388 | -0.0458 |
| seed_p_vs_seed_pars | 348 | -0.0927 | -0.0299 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
