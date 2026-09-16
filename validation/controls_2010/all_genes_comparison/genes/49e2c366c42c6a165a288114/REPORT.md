# YFR047C
Status: ok. Length: 971 nt. Measured usable bases: 613. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 613 | 0.4263 | 0.3867 |
| rnafold | ok | 613 | 0.4132 | 0.3839 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 246 | -0.0039 | -0.0107 |
| seed_p | 246 | -0.2107 | -0.1674 |
| seed_p_vs_seed_pars | 165 | -0.3935 | -0.3655 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
