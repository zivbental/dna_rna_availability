# YFR042W
Status: ok. Length: 748 nt. Measured usable bases: 402. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 402 | 0.3003 | 0.2984 |
| rnafold | ok | 402 | 0.2258 | 0.2350 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.2870 | 0.0036 |
| seed_p | 143 | 0.0109 | 0.0590 |
| seed_p_vs_seed_pars | 90 | -0.0681 | -0.0100 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
