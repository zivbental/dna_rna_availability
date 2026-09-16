# YIL067C
Status: ok. Length: 2074 nt. Measured usable bases: 850. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 850 | 0.3461 | 0.3326 |
| rnafold | ok | 850 | 0.2413 | 0.2286 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 59 | 0.1263 | 0.0218 |
| seed_p | 59 | 0.4144 | 0.3517 |
| seed_p_vs_seed_pars | 52 | 0.1310 | 0.2510 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
