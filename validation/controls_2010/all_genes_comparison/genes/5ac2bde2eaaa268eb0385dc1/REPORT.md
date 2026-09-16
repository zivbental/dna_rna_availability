# YGR078C
Status: ok. Length: 742 nt. Measured usable bases: 397. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 397 | 0.3332 | 0.3161 |
| rnafold | ok | 397 | 0.1916 | 0.1717 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 171 | 0.0057 | 0.0517 |
| seed_p | 171 | -0.1405 | 0.1479 |
| seed_p_vs_seed_pars | 119 | -0.4276 | -0.0147 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
