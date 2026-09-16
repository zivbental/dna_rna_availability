# YEL027W
Status: ok. Length: 788 nt. Measured usable bases: 695. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 695 | 0.3012 | 0.2778 |
| rnafold | ok | 695 | 0.2464 | 0.2401 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 682 | -0.2315 | -0.2631 |
| seed_p | 682 | -0.2690 | -0.2641 |
| seed_p_vs_seed_pars | 588 | -0.1872 | -0.1272 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
