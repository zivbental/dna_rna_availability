# YOR215C
Status: ok. Length: 727 nt. Measured usable bases: 305. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 305 | 0.3784 | 0.3588 |
| rnafold | ok | 305 | 0.2945 | 0.2849 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | -0.5958 | -0.7457 |
| seed_p | 60 | -0.1769 | -0.0776 |
| seed_p_vs_seed_pars | 55 | -0.5091 | -0.3933 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
