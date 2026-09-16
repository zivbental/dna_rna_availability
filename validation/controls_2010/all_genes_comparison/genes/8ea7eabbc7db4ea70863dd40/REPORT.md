# YJL097W
Status: ok. Length: 754 nt. Measured usable bases: 578. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 578 | 0.2503 | 0.2529 |
| rnafold | ok | 578 | 0.2409 | 0.2489 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 487 | -0.1157 | -0.2205 |
| seed_p | 487 | -0.2921 | -0.3112 |
| seed_p_vs_seed_pars | 369 | -0.5403 | -0.4586 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
