# YDR427W
Status: ok. Length: 1313 nt. Measured usable bases: 817. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 817 | 0.2461 | 0.2438 |
| rnafold | ok | 817 | 0.2123 | 0.2139 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 304 | -0.0148 | -0.0101 |
| seed_p | 304 | -0.1585 | -0.0255 |
| seed_p_vs_seed_pars | 230 | -0.2726 | -0.1514 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
