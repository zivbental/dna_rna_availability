# YMR217W
Status: ok. Length: 1704 nt. Measured usable bases: 1561. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1561 | 0.3645 | 0.3538 |
| rnafold | ok | 1561 | 0.2968 | 0.2857 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1565 | -0.2306 | -0.2590 |
| seed_p | 1565 | -0.1979 | -0.1809 |
| seed_p_vs_seed_pars | 1444 | -0.2199 | -0.1838 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
