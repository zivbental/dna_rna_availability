# YFL028C
Status: ok. Length: 953 nt. Measured usable bases: 499. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 499 | 0.3488 | 0.3340 |
| rnafold | ok | 499 | 0.3036 | 0.2982 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 150 | -0.1114 | -0.1229 |
| seed_p | 150 | -0.1705 | -0.1011 |
| seed_p_vs_seed_pars | 117 | -0.2786 | -0.1782 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
