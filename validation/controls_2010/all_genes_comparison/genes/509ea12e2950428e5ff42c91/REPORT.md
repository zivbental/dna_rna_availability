# YDR074W
Status: ok. Length: 3006 nt. Measured usable bases: 1519. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1519 | 0.3386 | 0.3275 |
| rnafold | ok | 1519 | 0.3104 | 0.3022 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 257 | -0.1614 | 0.0029 |
| seed_p | 257 | -0.0738 | 0.0541 |
| seed_p_vs_seed_pars | 193 | -0.1720 | -0.0458 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
