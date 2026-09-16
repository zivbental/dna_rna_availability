# YDR493W
Status: ok. Length: 560 nt. Measured usable bases: 245. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 245 | 0.4282 | 0.4267 |
| rnafold | ok | 245 | 0.2754 | 0.3103 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 38 | -0.6103 | -0.7159 |
| seed_p | 38 | -0.6577 | -0.4611 |
| seed_p_vs_seed_pars | 34 | -0.4596 | -0.0321 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
