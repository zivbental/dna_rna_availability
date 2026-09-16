# YBL102W
Status: ok. Length: 887 nt. Measured usable bases: 597. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 597 | 0.3587 | 0.3420 |
| rnafold | ok | 597 | 0.3087 | 0.2941 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 394 | -0.1363 | -0.1105 |
| seed_p | 394 | -0.2601 | -0.2357 |
| seed_p_vs_seed_pars | 329 | -0.3754 | -0.3751 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
