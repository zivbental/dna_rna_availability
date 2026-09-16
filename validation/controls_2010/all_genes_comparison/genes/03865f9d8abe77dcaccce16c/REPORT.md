# YFL014W
Status: ok. Length: 543 nt. Measured usable bases: 229. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 229 | 0.3912 | 0.3734 |
| rnafold | ok | 229 | 0.3429 | 0.3376 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | 0.6541 | 0.2139 |
| seed_p | 66 | 0.6051 | 0.2030 |
| seed_p_vs_seed_pars | 48 | -0.4691 | -0.3885 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
