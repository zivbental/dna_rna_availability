# YFR018C
Status: ok. Length: 1293 nt. Measured usable bases: 846. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 846 | 0.3035 | 0.2912 |
| rnafold | ok | 846 | 0.2802 | 0.2740 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 397 | 0.1168 | 0.1337 |
| seed_p | 397 | 0.0987 | 0.1766 |
| seed_p_vs_seed_pars | 275 | 0.1497 | 0.3029 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
