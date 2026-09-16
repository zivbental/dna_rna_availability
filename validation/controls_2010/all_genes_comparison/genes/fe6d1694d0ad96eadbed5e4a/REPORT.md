# YBR004C
Status: ok. Length: 1447 nt. Measured usable bases: 507. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 507 | 0.1908 | 0.1985 |
| rnafold | ok | 507 | 0.2054 | 0.1965 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | -0.2191 | -0.5895 |
| seed_p | 25 | -0.5873 | -0.7450 |
| seed_p_vs_seed_pars | 20 | 0.3550 | 0.1895 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
