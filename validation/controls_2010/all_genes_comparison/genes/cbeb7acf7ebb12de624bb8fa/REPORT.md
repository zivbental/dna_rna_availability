# YBR197C
Status: ok. Length: 820 nt. Measured usable bases: 401. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 401 | 0.3121 | 0.3082 |
| rnafold | ok | 401 | 0.3414 | 0.3277 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | 0.2487 | 0.8099 |
| seed_p | 50 | 0.5582 | 0.5733 |
| seed_p_vs_seed_pars | 47 | 0.5262 | 0.5426 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
