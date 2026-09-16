# YBR026C
Status: ok. Length: 1235 nt. Measured usable bases: 649.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 649 | 0.2798 | 0.2860 |
| rnafold | ok | 649 | 0.2775 | 0.2761 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 146 | 0.1171 | 0.3036 |
| seed_p | 146 | 0.2026 | 0.3308 |
| seed_p_vs_seed_pars | 104 | 0.0875 | 0.3572 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
