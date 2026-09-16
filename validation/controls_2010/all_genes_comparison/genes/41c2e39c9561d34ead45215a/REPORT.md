# YER031C
Status: ok. Length: 812 nt. Measured usable bases: 609. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 609 | 0.2495 | 0.2577 |
| rnafold | ok | 609 | 0.2146 | 0.2273 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 399 | 0.2119 | 0.1588 |
| seed_p | 399 | 0.0160 | 0.0515 |
| seed_p_vs_seed_pars | 334 | -0.2569 | -0.1632 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
