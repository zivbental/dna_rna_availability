# YOR319W
Status: ok. Length: 841 nt. Measured usable bases: 316. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 316 | 0.3656 | 0.3807 |
| rnafold | ok | 316 | 0.3559 | 0.3735 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | 0.0221 | 0.3865 |
| seed_p | 37 | 0.6874 | 0.4925 |
| seed_p_vs_seed_pars | 22 | -0.5775 | -0.1702 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
