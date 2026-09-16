# YOR209C
Status: ok. Length: 1523 nt. Measured usable bases: 1027. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1027 | 0.2845 | 0.2765 |
| rnafold | ok | 1027 | 0.2602 | 0.2546 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 552 | 0.1866 | 0.1045 |
| seed_p | 552 | 0.1403 | 0.0985 |
| seed_p_vs_seed_pars | 386 | -0.1093 | -0.0681 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
