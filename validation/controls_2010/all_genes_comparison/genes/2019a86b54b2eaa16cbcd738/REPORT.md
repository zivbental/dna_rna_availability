# YLR064W
Status: ok. Length: 950 nt. Measured usable bases: 508. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 508 | 0.2325 | 0.2152 |
| rnafold | ok | 508 | 0.1615 | 0.1524 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 156 | -0.1213 | -0.1752 |
| seed_p | 156 | -0.2807 | -0.3805 |
| seed_p_vs_seed_pars | 123 | -0.2540 | -0.3680 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
