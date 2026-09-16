# YBR256C
Status: ok. Length: 769 nt. Measured usable bases: 431. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 431 | 0.3755 | 0.3667 |
| rnafold | ok | 431 | 0.3005 | 0.2899 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 108 | -0.1679 | -0.3279 |
| seed_p | 108 | -0.2219 | -0.3844 |
| seed_p_vs_seed_pars | 89 | -0.2390 | -0.5087 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
