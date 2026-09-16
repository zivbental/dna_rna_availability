# YPL160W
Status: ok. Length: 3496 nt. Measured usable bases: 2649. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2649 | 0.3822 | 0.3670 |
| rnafold | ok | 2649 | 0.3120 | 0.3063 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1855 | -0.0710 | -0.1714 |
| seed_p | 1855 | -0.2216 | -0.1859 |
| seed_p_vs_seed_pars | 1423 | -0.3937 | -0.3626 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
