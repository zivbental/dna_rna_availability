# YLL031C
Status: ok. Length: 3259 nt. Measured usable bases: 1699. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1699 | 0.3035 | 0.2835 |
| rnafold | ok | 1699 | 0.2864 | 0.2778 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 422 | 0.0174 | 0.0606 |
| seed_p | 422 | -0.2616 | -0.3058 |
| seed_p_vs_seed_pars | 283 | -0.2119 | -0.2870 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
