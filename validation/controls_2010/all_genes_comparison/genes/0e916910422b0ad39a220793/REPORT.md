# YOL039W
Status: ok. Length: 645 nt. Measured usable bases: 444. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 444 | 0.3731 | 0.3519 |
| rnafold | ok | 444 | 0.3658 | 0.3637 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 335 | -0.0818 | -0.1858 |
| seed_p | 335 | -0.3464 | -0.3205 |
| seed_p_vs_seed_pars | 301 | -0.4664 | -0.3410 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
