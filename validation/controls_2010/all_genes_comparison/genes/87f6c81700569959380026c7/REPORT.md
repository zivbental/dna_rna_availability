# YNL175C
Status: ok. Length: 1302 nt. Measured usable bases: 700. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 700 | 0.3533 | 0.3527 |
| rnafold | ok | 700 | 0.3199 | 0.3202 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 180 | -0.1839 | -0.5294 |
| seed_p | 180 | -0.2823 | -0.4252 |
| seed_p_vs_seed_pars | 161 | -0.2741 | -0.3858 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
