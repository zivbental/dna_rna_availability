# YDR391C
Status: ok. Length: 788 nt. Measured usable bases: 335. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 335 | 0.2286 | 0.2108 |
| rnafold | ok | 335 | 0.1994 | 0.1783 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | -0.0510 | -0.6170 |
| seed_p | 60 | -0.3147 | -0.5353 |
| seed_p_vs_seed_pars | 38 | -0.7428 | -0.8525 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
