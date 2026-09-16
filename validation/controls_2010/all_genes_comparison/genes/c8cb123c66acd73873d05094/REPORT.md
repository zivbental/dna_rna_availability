# YGR161W-C
Status: ok. Length: 583 nt. Measured usable bases: 253. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 253 | 0.2863 | 0.2963 |
| rnafold | ok | 253 | 0.2603 | 0.2741 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | 0.0374 | -0.0561 |
| seed_p | 65 | -0.3833 | -0.1923 |
| seed_p_vs_seed_pars | 50 | 0.6141 | 0.4532 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
