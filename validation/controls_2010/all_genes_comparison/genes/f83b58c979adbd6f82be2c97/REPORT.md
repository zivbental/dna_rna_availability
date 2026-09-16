# YMR296C
Status: ok. Length: 1821 nt. Measured usable bases: 1402. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1402 | 0.2626 | 0.2506 |
| rnafold | ok | 1402 | 0.1978 | 0.1939 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1101 | -0.0858 | -0.1188 |
| seed_p | 1101 | -0.1214 | -0.0853 |
| seed_p_vs_seed_pars | 887 | -0.1456 | -0.0753 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
