# YOR273C
Status: ok. Length: 2190 nt. Measured usable bases: 1050. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1050 | 0.2393 | 0.2206 |
| rnafold | ok | 1050 | 0.2254 | 0.2141 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 190 | 0.1259 | -0.0332 |
| seed_p | 190 | 0.0987 | 0.0851 |
| seed_p_vs_seed_pars | 141 | 0.2558 | 0.2499 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
