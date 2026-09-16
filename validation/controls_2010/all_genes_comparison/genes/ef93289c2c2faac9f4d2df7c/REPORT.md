# YPR017C
Status: ok. Length: 591 nt. Measured usable bases: 323. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 323 | 0.4301 | 0.4224 |
| rnafold | ok | 323 | 0.3588 | 0.3631 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 132 | -0.2397 | -0.1536 |
| seed_p | 132 | -0.4408 | -0.2468 |
| seed_p_vs_seed_pars | 89 | -0.4345 | -0.5342 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
