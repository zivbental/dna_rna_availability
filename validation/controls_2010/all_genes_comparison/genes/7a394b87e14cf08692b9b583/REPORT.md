# YKL040C
Status: ok. Length: 1428 nt. Measured usable bases: 597. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 597 | 0.3152 | 0.3372 |
| rnafold | ok | 597 | 0.3181 | 0.3405 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | -0.0507 | -0.5111 |
| seed_p | 82 | -0.1191 | -0.2794 |
| seed_p_vs_seed_pars | 65 | -0.2358 | -0.4324 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
