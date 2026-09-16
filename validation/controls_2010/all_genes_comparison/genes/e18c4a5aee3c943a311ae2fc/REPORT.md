# YGR178C
Status: ok. Length: 2485 nt. Measured usable bases: 1548. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1548 | 0.3099 | 0.2999 |
| rnafold | ok | 1548 | 0.2890 | 0.2746 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 651 | 0.0803 | 0.0929 |
| seed_p | 651 | 0.1029 | 0.0418 |
| seed_p_vs_seed_pars | 457 | -0.0985 | -0.1131 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
