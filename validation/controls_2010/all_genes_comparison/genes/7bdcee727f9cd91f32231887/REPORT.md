# YLR214W
Status: ok. Length: 2325 nt. Measured usable bases: 1310. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1310 | 0.3652 | 0.3420 |
| rnafold | ok | 1310 | 0.2722 | 0.2706 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 455 | -0.1153 | -0.1177 |
| seed_p | 455 | -0.4353 | -0.3866 |
| seed_p_vs_seed_pars | 303 | -0.6416 | -0.5523 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
