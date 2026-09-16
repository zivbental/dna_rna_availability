# YGR014W
Status: ok. Length: 4057 nt. Measured usable bases: 2610. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2610 | 0.2717 | 0.2684 |
| rnafold | ok | 2610 | 0.2014 | 0.2057 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1398 | -0.0533 | -0.1978 |
| seed_p | 1398 | -0.1585 | -0.2311 |
| seed_p_vs_seed_pars | 1100 | -0.3201 | -0.3321 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
