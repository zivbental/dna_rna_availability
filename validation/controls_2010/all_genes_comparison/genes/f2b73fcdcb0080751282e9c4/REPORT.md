# YNL283C
Status: ok. Length: 1619 nt. Measured usable bases: 1023. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1023 | 0.2016 | 0.2050 |
| rnafold | ok | 1023 | 0.1903 | 0.2174 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 425 | 0.2986 | 0.0165 |
| seed_p | 425 | 0.3114 | 0.2759 |
| seed_p_vs_seed_pars | 322 | 0.1030 | 0.1579 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
