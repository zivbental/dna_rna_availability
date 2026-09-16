# YLR183C
Status: ok. Length: 1684 nt. Measured usable bases: 690. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 690 | 0.3245 | 0.3179 |
| rnafold | ok | 690 | 0.2482 | 0.2337 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | -0.3829 | -0.2347 |
| seed_p | 73 | -0.2163 | -0.2120 |
| seed_p_vs_seed_pars | 38 | -0.2510 | -0.3455 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
