# YDR224C
Status: ok. Length: 536 nt. Measured usable bases: 388. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 388 | 0.3656 | 0.3385 |
| rnafold | ok | 388 | 0.3743 | 0.3553 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 293 | -0.1844 | -0.2574 |
| seed_p | 293 | -0.2316 | -0.2301 |
| seed_p_vs_seed_pars | 255 | -0.3829 | -0.2727 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
