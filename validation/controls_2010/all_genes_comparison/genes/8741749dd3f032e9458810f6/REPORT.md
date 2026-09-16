# YOL158C
Status: ok. Length: 1971 nt. Measured usable bases: 1328. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1328 | 0.3075 | 0.2729 |
| rnafold | ok | 1328 | 0.2682 | 0.2321 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 718 | 0.0357 | 0.0916 |
| seed_p | 718 | -0.2116 | -0.0731 |
| seed_p_vs_seed_pars | 583 | -0.5912 | -0.3329 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
