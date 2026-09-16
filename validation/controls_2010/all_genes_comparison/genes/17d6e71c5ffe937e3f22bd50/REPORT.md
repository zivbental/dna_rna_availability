# YNR067C
Status: ok. Length: 3483 nt. Measured usable bases: 2499. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2499 | 0.2782 | 0.2663 |
| rnafold | ok | 2499 | 0.2260 | 0.2235 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1519 | -0.0642 | -0.1663 |
| seed_p | 1519 | -0.1401 | -0.1834 |
| seed_p_vs_seed_pars | 1159 | -0.2321 | -0.2747 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
