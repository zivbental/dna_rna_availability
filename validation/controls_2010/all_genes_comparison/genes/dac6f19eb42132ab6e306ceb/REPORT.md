# YKL008C
Status: ok. Length: 1464 nt. Measured usable bases: 1119. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1119 | 0.2981 | 0.2746 |
| rnafold | ok | 1119 | 0.2883 | 0.2835 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 852 | -0.1014 | -0.1097 |
| seed_p | 852 | -0.1867 | -0.1344 |
| seed_p_vs_seed_pars | 654 | -0.3298 | -0.2239 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
