# YER095W
Status: ok. Length: 1486 nt. Measured usable bases: 871. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 871 | 0.3629 | 0.3614 |
| rnafold | ok | 871 | 0.2979 | 0.3013 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 409 | -0.1846 | -0.2586 |
| seed_p | 409 | -0.2859 | -0.2829 |
| seed_p_vs_seed_pars | 319 | -0.3752 | -0.4345 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
