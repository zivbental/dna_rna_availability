# YNL305C
Status: ok. Length: 994 nt. Measured usable bases: 612. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 612 | 0.2825 | 0.2911 |
| rnafold | ok | 612 | 0.2505 | 0.2512 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 336 | -0.1030 | -0.2920 |
| seed_p | 336 | -0.0752 | -0.2040 |
| seed_p_vs_seed_pars | 259 | -0.1974 | -0.2208 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
