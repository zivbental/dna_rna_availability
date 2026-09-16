# YMR080C
Status: ok. Length: 3384 nt. Measured usable bases: 1869. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1869 | 0.2824 | 0.2670 |
| rnafold | ok | 1869 | 0.2577 | 0.2476 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 521 | 0.0171 | -0.0996 |
| seed_p | 521 | -0.0883 | -0.0950 |
| seed_p_vs_seed_pars | 391 | -0.1326 | -0.2058 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
