# YDR276C
Status: ok. Length: 418 nt. Measured usable bases: 334. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 334 | 0.2102 | 0.2250 |
| rnafold | ok | 334 | 0.2072 | 0.2395 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 307 | -0.1741 | -0.1434 |
| seed_p | 307 | -0.0085 | -0.0441 |
| seed_p_vs_seed_pars | 274 | 0.0350 | 0.0252 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
