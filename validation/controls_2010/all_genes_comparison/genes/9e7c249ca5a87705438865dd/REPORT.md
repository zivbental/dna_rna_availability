# YIL131C
Status: ok. Length: 1660 nt. Measured usable bases: 773. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 773 | 0.2142 | 0.2006 |
| rnafold | ok | 773 | 0.1810 | 0.1863 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 134 | 0.2471 | 0.2902 |
| seed_p | 134 | 0.0815 | 0.0956 |
| seed_p_vs_seed_pars | 109 | -0.3593 | -0.3936 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
