# YIR006C
Status: ok. Length: 4593 nt. Measured usable bases: 2249. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2249 | 0.3095 | 0.3029 |
| rnafold | ok | 2249 | 0.2611 | 0.2422 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 438 | 0.1319 | -0.0208 |
| seed_p | 438 | 0.1202 | 0.0363 |
| seed_p_vs_seed_pars | 332 | 0.0369 | 0.0106 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
