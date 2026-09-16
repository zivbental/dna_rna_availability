# YLR432W
Status: ok. Length: 1745 nt. Measured usable bases: 1044. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1044 | 0.3205 | 0.2861 |
| rnafold | ok | 1044 | 0.2956 | 0.2686 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 704 | -0.0563 | -0.0378 |
| seed_p | 704 | 0.0064 | -0.0708 |
| seed_p_vs_seed_pars | 642 | -0.0546 | -0.1155 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
