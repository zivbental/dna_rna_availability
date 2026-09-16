# YCL027W
Status: ok. Length: 1628 nt. Measured usable bases: 631. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 631 | 0.4053 | 0.4138 |
| rnafold | ok | 631 | 0.3427 | 0.3686 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 30 | 0.4362 | 0.2477 |
| seed_p | 30 | 0.2001 | 0.2279 |
| seed_p_vs_seed_pars | 22 | 0.5110 | 0.7048 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
