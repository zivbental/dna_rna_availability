# YMR127C
Status: ok. Length: 1259 nt. Measured usable bases: 445. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 445 | 0.3188 | 0.3208 |
| rnafold | ok | 445 | 0.2940 | 0.3121 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 26 | -0.8391 | -0.7005 |
| seed_p | 26 | -0.9307 | -0.9211 |
| seed_p_vs_seed_pars | 17 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
