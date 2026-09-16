# YMR005W
Status: ok. Length: 1301 nt. Measured usable bases: 607. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 607 | 0.3491 | 0.3757 |
| rnafold | ok | 607 | 0.3716 | 0.3899 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 126 | 0.1694 | 0.2948 |
| seed_p | 126 | -0.2762 | -0.2476 |
| seed_p_vs_seed_pars | 85 | -0.4039 | -0.3372 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
