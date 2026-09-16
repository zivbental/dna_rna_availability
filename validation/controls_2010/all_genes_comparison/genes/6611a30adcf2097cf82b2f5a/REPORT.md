# YPL227C
Status: ok. Length: 1197 nt. Measured usable bases: 554. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 554 | 0.2584 | 0.2637 |
| rnafold | ok | 554 | 0.2036 | 0.2144 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | 0.2086 | 0.2850 |
| seed_p | 121 | -0.2391 | -0.1386 |
| seed_p_vs_seed_pars | 70 | -0.2394 | -0.1908 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
