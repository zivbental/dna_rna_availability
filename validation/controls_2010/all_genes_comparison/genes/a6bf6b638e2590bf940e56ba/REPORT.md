# YDR293C
Status: ok. Length: 4253 nt. Measured usable bases: 2120. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2120 | 0.3408 | 0.3235 |
| rnafold | ok | 2120 | 0.3128 | 0.2947 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 382 | -0.2595 | -0.2681 |
| seed_p | 382 | -0.3541 | -0.3748 |
| seed_p_vs_seed_pars | 253 | -0.5522 | -0.6544 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
