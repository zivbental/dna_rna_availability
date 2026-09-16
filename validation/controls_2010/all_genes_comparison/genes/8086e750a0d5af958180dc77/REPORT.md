# YML115C
Status: ok. Length: 1684 nt. Measured usable bases: 983. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 983 | 0.2555 | 0.2417 |
| rnafold | ok | 983 | 0.1842 | 0.1649 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 378 | 0.0058 | -0.1135 |
| seed_p | 378 | -0.2956 | -0.1980 |
| seed_p_vs_seed_pars | 266 | -0.1828 | -0.0788 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
