# YNL138W
Status: ok. Length: 1761 nt. Measured usable bases: 1237. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1237 | 0.3192 | 0.3112 |
| rnafold | ok | 1237 | 0.2987 | 0.2930 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 759 | -0.1278 | -0.3011 |
| seed_p | 759 | -0.3509 | -0.3264 |
| seed_p_vs_seed_pars | 639 | -0.2610 | -0.1861 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
