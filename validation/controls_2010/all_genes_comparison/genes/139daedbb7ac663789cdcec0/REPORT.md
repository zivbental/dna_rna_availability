# YGR037C
Status: ok. Length: 460 nt. Measured usable bases: 388. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 388 | 0.4051 | 0.3748 |
| rnafold | ok | 388 | 0.3848 | 0.3701 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 317 | -0.3571 | -0.1740 |
| seed_p | 317 | -0.5402 | -0.4216 |
| seed_p_vs_seed_pars | 315 | -0.5238 | -0.4133 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
