# YDR385W
Status: ok. Length: 2710 nt. Measured usable bases: 191. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 191 | 0.3478 | 0.3195 |
| rnafold | ok | 191 | 0.3354 | 0.3100 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | -0.6452 | -0.3395 |
| seed_p | 81 | -0.5328 | -0.4761 |
| seed_p_vs_seed_pars | 63 | -0.1935 | -0.1819 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
