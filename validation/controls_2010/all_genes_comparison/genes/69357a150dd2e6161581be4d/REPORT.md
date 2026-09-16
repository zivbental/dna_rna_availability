# YBR016W
Status: ok. Length: 633 nt. Measured usable bases: 357. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 357 | 0.2662 | 0.2587 |
| rnafold | ok | 357 | 0.2849 | 0.2865 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 200 | -0.1139 | 0.0838 |
| seed_p | 200 | 0.1823 | 0.2907 |
| seed_p_vs_seed_pars | 184 | -0.1752 | -0.0934 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
