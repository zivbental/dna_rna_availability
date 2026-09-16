# YKL099C
Status: ok. Length: 906 nt. Measured usable bases: 387. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 387 | 0.3054 | 0.3119 |
| rnafold | ok | 387 | 0.3235 | 0.3317 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | 0.1329 | 0.0875 |
| seed_p | 54 | -0.1420 | -0.1176 |
| seed_p_vs_seed_pars | 53 | -0.4479 | -0.5985 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
