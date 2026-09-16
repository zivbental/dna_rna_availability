# YML101C
Status: ok. Length: 511 nt. Measured usable bases: 287. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 287 | 0.2994 | 0.3104 |
| rnafold | ok | 287 | 0.3216 | 0.3462 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 196 | 0.0397 | -0.0236 |
| seed_p | 196 | 0.3481 | 0.1301 |
| seed_p_vs_seed_pars | 155 | 0.3132 | 0.0362 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
