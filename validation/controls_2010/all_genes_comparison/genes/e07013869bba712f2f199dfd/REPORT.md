# YHR200W
Status: ok. Length: 906 nt. Measured usable bases: 674. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 674 | 0.2502 | 0.2283 |
| rnafold | ok | 674 | 0.2158 | 0.2032 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 639 | -0.0507 | -0.0803 |
| seed_p | 639 | -0.0978 | 0.0375 |
| seed_p_vs_seed_pars | 560 | -0.1499 | -0.0437 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
