# YER091C
Status: ok. Length: 2558 nt. Measured usable bases: 1871. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1871 | 0.3058 | 0.2839 |
| rnafold | ok | 1871 | 0.2447 | 0.2471 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1234 | -0.0053 | 0.0941 |
| seed_p | 1234 | -0.0792 | -0.0630 |
| seed_p_vs_seed_pars | 1017 | -0.2312 | -0.2519 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
