# YNL074C
Status: ok. Length: 1463 nt. Measured usable bases: 791. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 791 | 0.2778 | 0.2639 |
| rnafold | ok | 791 | 0.2350 | 0.2334 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 228 | -0.0534 | 0.1600 |
| seed_p | 228 | -0.1070 | -0.0142 |
| seed_p_vs_seed_pars | 159 | -0.3301 | -0.1605 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
