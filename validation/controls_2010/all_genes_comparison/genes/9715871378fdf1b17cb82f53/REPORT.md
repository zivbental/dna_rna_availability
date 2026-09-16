# YIL011W
Status: ok. Length: 955 nt. Measured usable bases: 327. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 327 | 0.2848 | 0.2821 |
| rnafold | ok | 327 | 0.2540 | 0.2771 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 23 | -0.2461 | 0.5192 |
| seed_p | 23 | 0.5384 | 0.6794 |
| seed_p_vs_seed_pars | 8 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
