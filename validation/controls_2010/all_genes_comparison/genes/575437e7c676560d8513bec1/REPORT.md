# YLR229C
Status: ok. Length: 642 nt. Measured usable bases: 507. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 507 | 0.2626 | 0.2634 |
| rnafold | ok | 507 | 0.3001 | 0.2978 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 423 | 0.2493 | 0.0390 |
| seed_p | 423 | 0.1122 | 0.1544 |
| seed_p_vs_seed_pars | 375 | 0.1936 | 0.1692 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
