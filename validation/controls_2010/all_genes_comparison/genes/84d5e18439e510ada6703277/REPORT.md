# YHR071W
Status: ok. Length: 808 nt. Measured usable bases: 410. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 410 | 0.2755 | 0.2672 |
| rnafold | ok | 410 | 0.2228 | 0.2412 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 94 | 0.1594 | -0.0570 |
| seed_p | 94 | 0.0061 | -0.1076 |
| seed_p_vs_seed_pars | 48 | -0.2995 | 0.1728 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
