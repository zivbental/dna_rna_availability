# YFL047W
Status: ok. Length: 2205 nt. Measured usable bases: 886. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 886 | 0.3539 | 0.3332 |
| rnafold | ok | 886 | 0.3421 | 0.3292 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.3167 | -0.4113 |
| seed_p | 58 | -0.2732 | 0.0255 |
| seed_p_vs_seed_pars | 36 | -0.4964 | -0.0866 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
