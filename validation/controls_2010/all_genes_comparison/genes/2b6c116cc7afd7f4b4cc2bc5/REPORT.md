# YLR100W
Status: ok. Length: 1157 nt. Measured usable bases: 933. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 933 | 0.3179 | 0.3058 |
| rnafold | ok | 933 | 0.2186 | 0.2455 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 806 | 0.0421 | -0.1031 |
| seed_p | 806 | -0.0428 | -0.0435 |
| seed_p_vs_seed_pars | 662 | -0.1389 | -0.2388 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
