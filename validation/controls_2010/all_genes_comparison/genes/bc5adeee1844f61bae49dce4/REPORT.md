# YKR079C
Status: ok. Length: 2658 nt. Measured usable bases: 1083. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1083 | 0.3014 | 0.2916 |
| rnafold | ok | 1083 | 0.2597 | 0.2519 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | -0.4419 | -0.3764 |
| seed_p | 92 | -0.5835 | -0.3273 |
| seed_p_vs_seed_pars | 58 | -0.7103 | -0.5964 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
