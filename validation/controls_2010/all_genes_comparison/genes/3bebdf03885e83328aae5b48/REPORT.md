# YLR412W
Status: ok. Length: 891 nt. Measured usable bases: 430. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 430 | 0.3827 | 0.3830 |
| rnafold | ok | 430 | 0.3497 | 0.3451 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | -0.4849 | 0.0312 |
| seed_p | 67 | -0.6679 | -0.6595 |
| seed_p_vs_seed_pars | 55 | -0.6621 | -0.4755 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
