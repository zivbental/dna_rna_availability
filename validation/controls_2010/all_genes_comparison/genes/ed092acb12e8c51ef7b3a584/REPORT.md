# YIL049W
Status: ok. Length: 838 nt. Measured usable bases: 339. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 339 | 0.2210 | 0.2269 |
| rnafold | ok | 339 | 0.1907 | 0.1924 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | 0.6301 | 0.7377 |
| seed_p | 28 | 0.0351 | -0.1628 |
| seed_p_vs_seed_pars | 8 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
