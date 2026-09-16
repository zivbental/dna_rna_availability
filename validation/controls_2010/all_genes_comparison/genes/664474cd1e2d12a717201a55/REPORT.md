# YHR030C
Status: ok. Length: 1661 nt. Measured usable bases: 756. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 756 | 0.2737 | 0.2863 |
| rnafold | ok | 756 | 0.2251 | 0.2584 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | 0.0080 | -0.0206 |
| seed_p | 137 | 0.1792 | 0.1987 |
| seed_p_vs_seed_pars | 114 | -0.0153 | 0.1248 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
