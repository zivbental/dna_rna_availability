# YGR267C
Status: ok. Length: 1007 nt. Measured usable bases: 625. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 625 | 0.2665 | 0.2652 |
| rnafold | ok | 625 | 0.2896 | 0.2989 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 397 | -0.0529 | -0.0405 |
| seed_p | 397 | -0.1464 | -0.1103 |
| seed_p_vs_seed_pars | 325 | -0.1760 | -0.0786 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
