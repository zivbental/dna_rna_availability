# YDR394W
Status: ok. Length: 1467 nt. Measured usable bases: 1162. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1162 | 0.3355 | 0.3285 |
| rnafold | ok | 1162 | 0.2666 | 0.2503 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1014 | -0.0993 | -0.1718 |
| seed_p | 1014 | -0.2345 | -0.2419 |
| seed_p_vs_seed_pars | 828 | -0.3720 | -0.3749 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
