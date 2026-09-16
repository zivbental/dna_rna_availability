# YBR079C
Status: ok. Length: 2985 nt. Measured usable bases: 2145.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2145 | 0.3831 | 0.3620 |
| rnafold | ok | 2145 | 0.2708 | 0.2617 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1343 | -0.0320 | -0.1775 |
| seed_p | 1343 | -0.2211 | -0.2326 |
| seed_p_vs_seed_pars | 1031 | -0.3855 | -0.3988 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
