# YHR061C
Status: ok. Length: 1382 nt. Measured usable bases: 471. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 471 | 0.1229 | 0.1253 |
| rnafold | ok | 471 | 0.0165 | 0.0402 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 59 | 0.3002 | 0.4556 |
| seed_p | 59 | 0.0683 | 0.1986 |
| seed_p_vs_seed_pars | 46 | -0.1651 | 0.2271 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
