# YIL123W
Status: ok. Length: 2250 nt. Measured usable bases: 1492. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1492 | 0.3709 | 0.3580 |
| rnafold | ok | 1492 | 0.2848 | 0.2708 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1167 | -0.1676 | -0.2721 |
| seed_p | 1167 | -0.3186 | -0.3523 |
| seed_p_vs_seed_pars | 1016 | -0.3999 | -0.4148 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
