# YOR149C
Status: ok. Length: 1627 nt. Measured usable bases: 786. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 786 | 0.2676 | 0.2529 |
| rnafold | ok | 786 | 0.1656 | 0.1602 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 236 | -0.1908 | 0.1035 |
| seed_p | 236 | -0.4741 | -0.3694 |
| seed_p_vs_seed_pars | 131 | -0.6869 | -0.6647 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
