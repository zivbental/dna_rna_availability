# YKL130C
Status: ok. Length: 903 nt. Measured usable bases: 491. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 491 | 0.3372 | 0.3203 |
| rnafold | ok | 491 | 0.3526 | 0.3491 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 163 | -0.6974 | -0.1280 |
| seed_p | 163 | -0.5737 | -0.0988 |
| seed_p_vs_seed_pars | 122 | -0.6740 | -0.4855 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
