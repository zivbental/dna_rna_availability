# YDR531W
Status: ok. Length: 1230 nt. Measured usable bases: 727. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 727 | 0.3377 | 0.3255 |
| rnafold | ok | 727 | 0.2876 | 0.2799 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 250 | -0.0536 | 0.0483 |
| seed_p | 250 | -0.1337 | -0.0133 |
| seed_p_vs_seed_pars | 189 | -0.2167 | -0.1564 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
