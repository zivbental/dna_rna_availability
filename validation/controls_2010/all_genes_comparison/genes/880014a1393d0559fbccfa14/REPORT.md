# YMR205C
Status: ok. Length: 3237 nt. Measured usable bases: 2786. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2786 | 0.2915 | 0.2756 |
| rnafold | ok | 2786 | 0.2808 | 0.2718 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2657 | -0.0044 | -0.0592 |
| seed_p | 2657 | -0.0979 | -0.0958 |
| seed_p_vs_seed_pars | 2269 | -0.1269 | -0.1355 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
