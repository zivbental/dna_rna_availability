# YER014W
Status: ok. Length: 1761 nt. Measured usable bases: 616. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 616 | 0.4007 | 0.3879 |
| rnafold | ok | 616 | 0.3665 | 0.3524 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | 0.1673 | -0.1215 |
| seed_p | 42 | 0.1937 | 0.2024 |
| seed_p_vs_seed_pars | 29 | -0.5683 | -0.7023 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
