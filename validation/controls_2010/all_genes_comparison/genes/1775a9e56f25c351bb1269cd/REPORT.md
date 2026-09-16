# YHR058C
Status: ok. Length: 978 nt. Measured usable bases: 402. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 402 | 0.3888 | 0.3686 |
| rnafold | ok | 402 | 0.3249 | 0.3045 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | -0.0661 | -0.2525 |
| seed_p | 61 | -0.2853 | -0.1199 |
| seed_p_vs_seed_pars | 46 | -0.4894 | -0.4375 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
