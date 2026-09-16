# YML096W
Status: ok. Length: 1693 nt. Measured usable bases: 704. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 704 | 0.2956 | 0.2973 |
| rnafold | ok | 704 | 0.2846 | 0.2787 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.2057 | -0.0447 |
| seed_p | 57 | 0.5798 | 0.3431 |
| seed_p_vs_seed_pars | 44 | 0.5234 | 0.4277 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
