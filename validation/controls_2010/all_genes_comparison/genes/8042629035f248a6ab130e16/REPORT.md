# YBR260C
Status: ok. Length: 2123 nt. Measured usable bases: 786. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 786 | 0.2581 | 0.2547 |
| rnafold | ok | 786 | 0.2157 | 0.2189 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | -0.2382 | 0.1161 |
| seed_p | 49 | -0.2080 | 0.0233 |
| seed_p_vs_seed_pars | 22 | 0.1998 | 0.5070 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
