# YFL022C
Status: ok. Length: 1666 nt. Measured usable bases: 1325. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1325 | 0.2867 | 0.2694 |
| rnafold | ok | 1325 | 0.2859 | 0.2716 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1129 | -0.0019 | -0.0535 |
| seed_p | 1129 | -0.1795 | -0.1744 |
| seed_p_vs_seed_pars | 1002 | -0.3307 | -0.2887 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
