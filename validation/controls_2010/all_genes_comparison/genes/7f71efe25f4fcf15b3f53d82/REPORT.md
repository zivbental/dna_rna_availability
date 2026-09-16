# YDR225W
Status: ok. Length: 617 nt. Measured usable bases: 387. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 387 | 0.3651 | 0.3795 |
| rnafold | ok | 387 | 0.3328 | 0.3539 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 255 | -0.1291 | -0.3887 |
| seed_p | 255 | -0.2359 | -0.4410 |
| seed_p_vs_seed_pars | 229 | -0.1475 | -0.3463 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
