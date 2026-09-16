# YOR046C
Status: ok. Length: 1534 nt. Measured usable bases: 1003. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1003 | 0.2832 | 0.2760 |
| rnafold | ok | 1003 | 0.2870 | 0.2973 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 473 | -0.2195 | -0.3501 |
| seed_p | 473 | -0.1983 | -0.3522 |
| seed_p_vs_seed_pars | 343 | -0.2887 | -0.5711 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
