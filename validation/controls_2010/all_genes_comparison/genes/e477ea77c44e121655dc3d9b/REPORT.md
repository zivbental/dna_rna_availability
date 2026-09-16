# YKL196C
Status: ok. Length: 777 nt. Measured usable bases: 565. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 565 | 0.3952 | 0.3729 |
| rnafold | ok | 565 | 0.3131 | 0.3006 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 391 | 0.2546 | 0.2052 |
| seed_p | 391 | -0.1639 | -0.1429 |
| seed_p_vs_seed_pars | 324 | -0.4163 | -0.2857 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
