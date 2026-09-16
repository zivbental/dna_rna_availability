# YOL005C
Status: ok. Length: 416 nt. Measured usable bases: 335. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 335 | 0.3367 | 0.3142 |
| rnafold | ok | 335 | 0.2594 | 0.2581 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 304 | 0.0433 | 0.0406 |
| seed_p | 304 | 0.0513 | 0.1270 |
| seed_p_vs_seed_pars | 234 | -0.4637 | -0.3581 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
