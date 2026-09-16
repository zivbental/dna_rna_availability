# YCL043C
Status: ok. Length: 1682 nt. Measured usable bases: 1554. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1554 | 0.2866 | 0.2632 |
| rnafold | ok | 1554 | 0.2415 | 0.2194 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1547 | -0.0581 | -0.1125 |
| seed_p | 1547 | -0.1039 | -0.1514 |
| seed_p_vs_seed_pars | 1471 | -0.2059 | -0.2780 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
