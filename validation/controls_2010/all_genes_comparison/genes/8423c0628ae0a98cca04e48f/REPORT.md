# YLL024C
Status: ok. Length: 2057 nt. Measured usable bases: 556. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 556 | 0.2844 | 0.2637 |
| rnafold | ok | 556 | 0.1749 | 0.1656 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 343 | 0.1062 | -0.1418 |
| seed_p | 343 | -0.2105 | -0.1522 |
| seed_p_vs_seed_pars | 260 | -0.3807 | -0.3310 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
