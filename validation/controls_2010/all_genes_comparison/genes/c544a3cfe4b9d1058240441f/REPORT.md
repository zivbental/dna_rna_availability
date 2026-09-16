# YKL128C
Status: ok. Length: 1043 nt. Measured usable bases: 716. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 716 | 0.3444 | 0.3441 |
| rnafold | ok | 716 | 0.2595 | 0.2788 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 399 | -0.0338 | -0.2512 |
| seed_p | 399 | -0.3897 | -0.3661 |
| seed_p_vs_seed_pars | 277 | -0.3676 | -0.4164 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
