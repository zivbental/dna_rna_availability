# YGR020C
Status: ok. Length: 541 nt. Measured usable bases: 437. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 437 | 0.2974 | 0.3285 |
| rnafold | ok | 437 | 0.1758 | 0.2155 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 379 | -0.0980 | 0.1343 |
| seed_p | 379 | -0.0852 | 0.1118 |
| seed_p_vs_seed_pars | 356 | -0.0287 | 0.0816 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
