# YGR123C
Status: ok. Length: 1702 nt. Measured usable bases: 882. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 882 | 0.2674 | 0.2503 |
| rnafold | ok | 882 | 0.2615 | 0.2421 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | 0.0288 | 0.0259 |
| seed_p | 143 | -0.2323 | -0.2387 |
| seed_p_vs_seed_pars | 78 | -0.2621 | -0.4342 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
