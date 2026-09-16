# YCL050C
Status: ok. Length: 1115 nt. Measured usable bases: 765. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 765 | 0.1971 | 0.1947 |
| rnafold | ok | 765 | 0.1415 | 0.1522 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 520 | -0.3178 | -0.4293 |
| seed_p | 520 | -0.2894 | -0.2906 |
| seed_p_vs_seed_pars | 422 | -0.2779 | -0.3587 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
