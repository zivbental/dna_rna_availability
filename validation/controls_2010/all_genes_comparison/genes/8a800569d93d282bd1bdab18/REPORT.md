# YDR286C
Status: ok. Length: 469 nt. Measured usable bases: 172. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 172 | 0.4812 | 0.4746 |
| rnafold | ok | 172 | 0.4070 | 0.4154 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 27 | -0.7335 | -0.8235 |
| seed_p | 27 | -0.1259 | -0.1303 |
| seed_p_vs_seed_pars | 18 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
