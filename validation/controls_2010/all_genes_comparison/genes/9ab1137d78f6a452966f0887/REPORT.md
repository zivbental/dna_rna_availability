# YER157W
Status: ok. Length: 2406 nt. Measured usable bases: 952. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 952 | 0.2917 | 0.2802 |
| rnafold | ok | 952 | 0.1923 | 0.1986 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | 0.2393 | 0.3169 |
| seed_p | 61 | -0.5193 | -0.1910 |
| seed_p_vs_seed_pars | 33 | 0.2480 | 0.1688 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
