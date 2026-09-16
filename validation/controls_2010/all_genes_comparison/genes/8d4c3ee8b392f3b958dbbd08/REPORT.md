# YNL118C
Status: ok. Length: 3072 nt. Measured usable bases: 1249. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1249 | 0.3316 | 0.3268 |
| rnafold | ok | 1249 | 0.3081 | 0.3040 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 147 | 0.0617 | 0.1162 |
| seed_p | 147 | 0.1711 | 0.2261 |
| seed_p_vs_seed_pars | 123 | 0.0380 | 0.0665 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
