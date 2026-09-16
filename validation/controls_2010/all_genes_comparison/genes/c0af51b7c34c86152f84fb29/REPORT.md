# YLR441C
Status: ok. Length: 974 nt. Measured usable bases: 597. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 597 | 0.2677 | 0.2353 |
| rnafold | ok | 597 | 0.2473 | 0.2508 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 352 | 0.1154 | -0.1040 |
| seed_p | 352 | -0.0448 | -0.0999 |
| seed_p_vs_seed_pars | 323 | -0.1012 | -0.2026 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
