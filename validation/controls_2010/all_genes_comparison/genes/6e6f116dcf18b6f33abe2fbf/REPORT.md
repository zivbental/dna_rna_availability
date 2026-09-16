# YCL018W
Status: ok. Length: 1095 nt. Measured usable bases: 711. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 711 | 0.2941 | 0.2814 |
| rnafold | ok | 711 | 0.2053 | 0.2380 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 383 | 0.0677 | -0.0241 |
| seed_p | 383 | -0.0826 | 0.0244 |
| seed_p_vs_seed_pars | 322 | -0.1384 | -0.0497 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
