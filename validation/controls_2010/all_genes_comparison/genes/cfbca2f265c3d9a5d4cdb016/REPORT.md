# YOR034C
Status: ok. Length: 2351 nt. Measured usable bases: 1034. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1034 | 0.2788 | 0.2527 |
| rnafold | ok | 1034 | 0.2159 | 0.2048 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | -0.1589 | -0.0252 |
| seed_p | 137 | 0.0143 | 0.2523 |
| seed_p_vs_seed_pars | 108 | -0.1337 | 0.1220 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
