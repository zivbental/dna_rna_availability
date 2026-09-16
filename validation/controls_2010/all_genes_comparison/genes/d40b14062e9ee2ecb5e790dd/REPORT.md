# YKL033W-A
Status: ok. Length: 870 nt. Measured usable bases: 638. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 638 | 0.3992 | 0.3892 |
| rnafold | ok | 638 | 0.3421 | 0.3304 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 494 | -0.1898 | -0.1864 |
| seed_p | 494 | -0.1595 | -0.1437 |
| seed_p_vs_seed_pars | 441 | -0.2819 | -0.2059 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
