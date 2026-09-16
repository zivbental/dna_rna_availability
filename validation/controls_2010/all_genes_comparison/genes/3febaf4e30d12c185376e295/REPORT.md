# YIR035C
Status: ok. Length: 847 nt. Measured usable bases: 544. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 544 | 0.3333 | 0.3072 |
| rnafold | ok | 544 | 0.2600 | 0.2379 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 323 | -0.3007 | -0.0489 |
| seed_p | 323 | -0.2389 | -0.2111 |
| seed_p_vs_seed_pars | 249 | -0.1127 | -0.0872 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
