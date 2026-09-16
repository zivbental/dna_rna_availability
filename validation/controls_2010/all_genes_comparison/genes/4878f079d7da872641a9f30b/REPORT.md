# YKL057C
Status: ok. Length: 3186 nt. Measured usable bases: 1317. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1317 | 0.2677 | 0.2525 |
| rnafold | ok | 1317 | 0.2156 | 0.2026 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 152 | 0.0951 | 0.3907 |
| seed_p | 152 | 0.2883 | 0.2035 |
| seed_p_vs_seed_pars | 108 | -0.1330 | -0.2258 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
