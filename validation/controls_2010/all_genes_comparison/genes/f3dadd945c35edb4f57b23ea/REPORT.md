# YLR196W
Status: ok. Length: 1936 nt. Measured usable bases: 888. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 888 | 0.2607 | 0.2581 |
| rnafold | ok | 888 | 0.3183 | 0.3005 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 132 | 0.3006 | 0.3963 |
| seed_p | 132 | -0.0625 | -0.0805 |
| seed_p_vs_seed_pars | 85 | -0.0206 | -0.0786 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
