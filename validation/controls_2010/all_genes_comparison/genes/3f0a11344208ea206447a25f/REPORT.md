# YLR437C
Status: ok. Length: 498 nt. Measured usable bases: 296. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 296 | 0.2699 | 0.2629 |
| rnafold | ok | 296 | 0.2072 | 0.1814 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | -0.2588 | -0.1173 |
| seed_p | 135 | -0.1868 | -0.1143 |
| seed_p_vs_seed_pars | 97 | 0.2314 | 0.0637 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
