# YIL035C
Status: ok. Length: 1319 nt. Measured usable bases: 488. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 488 | 0.2413 | 0.2305 |
| rnafold | ok | 488 | 0.2639 | 0.2496 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | -0.1237 | 0.2718 |
| seed_p | 54 | -0.0487 | -0.0884 |
| seed_p_vs_seed_pars | 41 | -0.3250 | -0.3853 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
