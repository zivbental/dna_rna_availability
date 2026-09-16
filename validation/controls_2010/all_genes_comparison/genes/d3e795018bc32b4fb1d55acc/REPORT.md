# YDL070W
Status: ok. Length: 2072 nt. Measured usable bases: 824. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 824 | 0.2717 | 0.2551 |
| rnafold | ok | 824 | 0.3148 | 0.2792 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 158 | -0.0047 | -0.0866 |
| seed_p | 158 | -0.1665 | -0.2542 |
| seed_p_vs_seed_pars | 118 | -0.2450 | -0.3085 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
