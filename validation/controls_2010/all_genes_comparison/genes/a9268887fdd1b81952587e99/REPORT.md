# YBR158W
Status: ok. Length: 2062 nt. Measured usable bases: 1382. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1382 | 0.2934 | 0.2720 |
| rnafold | ok | 1382 | 0.2312 | 0.2088 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 866 | -0.1116 | -0.1552 |
| seed_p | 866 | -0.1762 | -0.1107 |
| seed_p_vs_seed_pars | 689 | -0.2966 | -0.2535 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
