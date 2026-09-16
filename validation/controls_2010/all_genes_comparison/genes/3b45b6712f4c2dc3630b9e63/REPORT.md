# YKR087C
Status: ok. Length: 1156 nt. Measured usable bases: 432. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 432 | 0.3991 | 0.3896 |
| rnafold | ok | 432 | 0.3035 | 0.2823 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | -0.3656 | -0.6659 |
| seed_p | 34 | -0.4876 | -0.5961 |
| seed_p_vs_seed_pars | 34 | -0.3672 | -0.4083 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
