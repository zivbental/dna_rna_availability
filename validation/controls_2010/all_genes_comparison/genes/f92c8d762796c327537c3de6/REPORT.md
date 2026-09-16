# YHR113W
Status: ok. Length: 1586 nt. Measured usable bases: 985. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 985 | 0.2995 | 0.2869 |
| rnafold | ok | 985 | 0.3012 | 0.2951 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 383 | 0.2358 | 0.1231 |
| seed_p | 383 | -0.0205 | -0.0372 |
| seed_p_vs_seed_pars | 285 | 0.0328 | 0.0358 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
