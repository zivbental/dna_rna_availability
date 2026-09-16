# YHR138C
Status: ok. Length: 478 nt. Measured usable bases: 204. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 204 | 0.2765 | 0.2696 |
| rnafold | ok | 204 | 0.1174 | 0.0971 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 27 | 0.1687 | -0.0391 |
| seed_p | 27 | -0.5642 | -0.6166 |
| seed_p_vs_seed_pars | 17 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
