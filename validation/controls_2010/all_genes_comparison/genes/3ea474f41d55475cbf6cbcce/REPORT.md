# YBR162W-A
Status: ok. Length: 363 nt. Measured usable bases: 229. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 229 | 0.3409 | 0.3591 |
| rnafold | ok | 229 | 0.3091 | 0.3597 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 129 | -0.0323 | 0.0227 |
| seed_p | 129 | 0.0529 | -0.0346 |
| seed_p_vs_seed_pars | 115 | 0.2567 | 0.1486 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
