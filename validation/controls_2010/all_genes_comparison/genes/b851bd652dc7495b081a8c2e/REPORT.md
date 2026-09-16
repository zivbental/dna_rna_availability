# YBR154C
Status: ok. Length: 832 nt. Measured usable bases: 465. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 465 | 0.2323 | 0.2516 |
| rnafold | ok | 465 | 0.2247 | 0.2401 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 158 | 0.1343 | -0.2721 |
| seed_p | 158 | -0.3817 | -0.2439 |
| seed_p_vs_seed_pars | 106 | -0.5774 | -0.3403 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
