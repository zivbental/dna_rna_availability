# YJL069C
Status: ok. Length: 1875 nt. Measured usable bases: 938. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 938 | 0.2360 | 0.2408 |
| rnafold | ok | 938 | 0.2145 | 0.2187 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 122 | 0.3930 | -0.0191 |
| seed_p | 122 | 0.2231 | 0.1255 |
| seed_p_vs_seed_pars | 79 | 0.5583 | 0.3093 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
