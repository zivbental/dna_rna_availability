# YJL122W
Status: ok. Length: 714 nt. Measured usable bases: 393. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 393 | 0.3805 | 0.4031 |
| rnafold | ok | 393 | 0.3157 | 0.3330 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 105 | 0.5568 | 0.0750 |
| seed_p | 105 | 0.1398 | -0.0077 |
| seed_p_vs_seed_pars | 82 | -0.1785 | -0.2474 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
