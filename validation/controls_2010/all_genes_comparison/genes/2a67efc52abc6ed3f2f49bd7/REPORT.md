# YOR374W
Status: ok. Length: 1825 nt. Measured usable bases: 922. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 922 | 0.3610 | 0.3537 |
| rnafold | ok | 922 | 0.2811 | 0.2635 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 217 | 0.0916 | 0.1849 |
| seed_p | 217 | 0.0929 | 0.0358 |
| seed_p_vs_seed_pars | 148 | 0.1031 | 0.1236 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
