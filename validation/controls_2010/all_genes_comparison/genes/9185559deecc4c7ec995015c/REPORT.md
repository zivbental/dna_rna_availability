# YLR144C
Status: ok. Length: 2400 nt. Measured usable bases: 974. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 974 | 0.2877 | 0.2596 |
| rnafold | ok | 974 | 0.2549 | 0.2382 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | 0.4134 | 0.4496 |
| seed_p | 45 | -0.0855 | -0.3328 |
| seed_p_vs_seed_pars | 35 | -0.3274 | -0.4212 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
