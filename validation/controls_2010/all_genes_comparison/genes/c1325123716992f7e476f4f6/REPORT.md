# YNL108C
Status: ok. Length: 970 nt. Measured usable bases: 546. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 546 | 0.3310 | 0.3293 |
| rnafold | ok | 546 | 0.2338 | 0.2596 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 192 | -0.1142 | -0.0967 |
| seed_p | 192 | -0.0852 | -0.0176 |
| seed_p_vs_seed_pars | 149 | 0.0065 | 0.1535 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
