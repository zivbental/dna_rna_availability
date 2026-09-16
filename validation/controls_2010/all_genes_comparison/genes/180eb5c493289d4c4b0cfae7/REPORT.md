# YER141W
Status: ok. Length: 2711 nt. Measured usable bases: 710. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 710 | 0.3607 | 0.3588 |
| rnafold | ok | 710 | 0.2250 | 0.2161 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 309 | -0.1748 | -0.4087 |
| seed_p | 309 | -0.2243 | -0.3353 |
| seed_p_vs_seed_pars | 252 | -0.1794 | -0.3185 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
