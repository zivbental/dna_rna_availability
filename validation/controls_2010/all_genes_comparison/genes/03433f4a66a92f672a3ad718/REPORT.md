# YFR025C
Status: ok. Length: 1124 nt. Measured usable bases: 723. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 723 | 0.3455 | 0.3404 |
| rnafold | ok | 723 | 0.2825 | 0.2655 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 315 | -0.3665 | -0.1699 |
| seed_p | 315 | -0.3441 | -0.2590 |
| seed_p_vs_seed_pars | 214 | -0.4764 | -0.4807 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
