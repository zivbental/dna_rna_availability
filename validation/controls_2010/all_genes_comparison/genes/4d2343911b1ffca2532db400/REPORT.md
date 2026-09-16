# YKR080W
Status: ok. Length: 1265 nt. Measured usable bases: 712. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 712 | 0.2986 | 0.3037 |
| rnafold | ok | 712 | 0.2666 | 0.2708 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 210 | 0.5958 | 0.0575 |
| seed_p | 210 | 0.0477 | -0.1729 |
| seed_p_vs_seed_pars | 158 | 0.0430 | -0.2065 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
