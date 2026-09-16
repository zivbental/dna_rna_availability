# YOR375C
Status: ok. Length: 1503 nt. Measured usable bases: 1033. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1033 | 0.2705 | 0.2621 |
| rnafold | ok | 1033 | 0.1682 | 0.1921 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 645 | 0.0489 | 0.2489 |
| seed_p | 645 | 0.0728 | 0.1307 |
| seed_p_vs_seed_pars | 516 | 0.0970 | 0.1627 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
