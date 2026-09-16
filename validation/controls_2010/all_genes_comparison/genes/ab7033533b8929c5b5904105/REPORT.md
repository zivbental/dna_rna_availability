# YKL211C
Status: ok. Length: 1635 nt. Measured usable bases: 1165. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1165 | 0.3236 | 0.3150 |
| rnafold | ok | 1165 | 0.3042 | 0.2999 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 760 | -0.1386 | -0.2247 |
| seed_p | 760 | -0.1688 | -0.0775 |
| seed_p_vs_seed_pars | 599 | -0.1617 | -0.2234 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
