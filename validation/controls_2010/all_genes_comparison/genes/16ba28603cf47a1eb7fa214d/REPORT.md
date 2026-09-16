# YGL140C
Status: ok. Length: 3923 nt. Measured usable bases: 1478. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1478 | 0.3244 | 0.3087 |
| rnafold | ok | 1478 | 0.2897 | 0.2712 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 99 | 0.0856 | -0.0317 |
| seed_p | 99 | -0.2355 | -0.1896 |
| seed_p_vs_seed_pars | 74 | -0.5244 | -0.6312 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
