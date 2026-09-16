# YLR449W
Status: ok. Length: 1296 nt. Measured usable bases: 749. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 749 | 0.3771 | 0.4064 |
| rnafold | ok | 749 | 0.3975 | 0.4109 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 330 | -0.3489 | -0.2517 |
| seed_p | 330 | -0.4208 | -0.3809 |
| seed_p_vs_seed_pars | 244 | -0.5739 | -0.5538 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
