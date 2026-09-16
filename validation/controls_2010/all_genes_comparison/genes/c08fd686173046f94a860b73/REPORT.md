# YBR261C
Status: ok. Length: 834 nt. Measured usable bases: 545. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 545 | 0.4581 | 0.4447 |
| rnafold | ok | 545 | 0.3750 | 0.3617 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 281 | -0.6226 | -0.0105 |
| seed_p | 281 | -0.6330 | -0.2552 |
| seed_p_vs_seed_pars | 245 | -0.7924 | -0.7273 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
