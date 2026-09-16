# YBL089W
Status: ok. Length: 1475 nt. Measured usable bases: 609.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 609 | 0.2747 | 0.2463 |
| rnafold | ok | 609 | 0.1319 | 0.1207 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 53 | -0.6756 | -0.7511 |
| seed_p | 53 | -0.4642 | -0.5994 |
| seed_p_vs_seed_pars | 29 | -0.0874 | -0.6467 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
