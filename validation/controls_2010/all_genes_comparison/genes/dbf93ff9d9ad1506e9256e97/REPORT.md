# YMR301C
Status: ok. Length: 2247 nt. Measured usable bases: 833. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 833 | 0.3371 | 0.3140 |
| rnafold | ok | 833 | 0.3004 | 0.2758 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 86 | -0.0437 | 0.1872 |
| seed_p | 86 | 0.3878 | 0.2583 |
| seed_p_vs_seed_pars | 54 | 0.5791 | 0.4614 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
