# YIR021W
Status: ok. Length: 1136 nt. Measured usable bases: 562. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 562 | 0.2661 | 0.2617 |
| rnafold | ok | 562 | 0.2114 | 0.2198 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | 0.1765 | 0.1644 |
| seed_p | 118 | 0.2972 | 0.4293 |
| seed_p_vs_seed_pars | 103 | 0.3883 | 0.3129 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
