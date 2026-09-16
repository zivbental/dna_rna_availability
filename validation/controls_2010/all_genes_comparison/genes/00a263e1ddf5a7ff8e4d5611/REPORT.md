# YOL040C
Status: ok. Length: 529 nt. Measured usable bases: 501. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 501 | 0.2703 | 0.2485 |
| rnafold | ok | 501 | 0.3039 | 0.2801 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 487 | -0.0574 | -0.2330 |
| seed_p | 487 | -0.3830 | -0.3282 |
| seed_p_vs_seed_pars | 486 | -0.3919 | -0.3246 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
