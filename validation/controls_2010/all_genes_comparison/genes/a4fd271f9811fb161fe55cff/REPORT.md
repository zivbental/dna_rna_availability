# YPR011C
Status: ok. Length: 1372 nt. Measured usable bases: 497. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 497 | 0.3795 | 0.3588 |
| rnafold | ok | 497 | 0.3370 | 0.3087 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | -0.4451 | -0.3757 |
| seed_p | 25 | -0.5518 | -0.4526 |
| seed_p_vs_seed_pars | 7 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
