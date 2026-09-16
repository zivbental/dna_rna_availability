# YLR361C
Status: ok. Length: 2085 nt. Measured usable bases: 809. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 809 | 0.2658 | 0.2697 |
| rnafold | ok | 809 | 0.2059 | 0.2081 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | -0.6567 | -0.8338 |
| seed_p | 37 | -0.1238 | -0.1564 |
| seed_p_vs_seed_pars | 24 | -0.4799 | -0.3933 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
