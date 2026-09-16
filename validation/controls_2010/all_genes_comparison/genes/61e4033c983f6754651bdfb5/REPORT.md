# YNL131W
Status: ok. Length: 996 nt. Measured usable bases: 604. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 604 | 0.2128 | 0.1869 |
| rnafold | ok | 604 | 0.0946 | 0.0899 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 447 | -0.0135 | 0.0305 |
| seed_p | 447 | 0.2484 | 0.2569 |
| seed_p_vs_seed_pars | 416 | 0.2283 | 0.2187 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
