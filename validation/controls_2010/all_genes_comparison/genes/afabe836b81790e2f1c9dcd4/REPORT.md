# YNL070W
Status: ok. Length: 382 nt. Measured usable bases: 237. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 237 | 0.2637 | 0.2460 |
| rnafold | ok | 237 | 0.2133 | 0.1795 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 162 | 0.0029 | 0.0417 |
| seed_p | 162 | -0.0272 | -0.0682 |
| seed_p_vs_seed_pars | 110 | -0.3111 | -0.3696 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
