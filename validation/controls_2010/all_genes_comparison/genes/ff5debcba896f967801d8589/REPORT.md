# YJR058C
Status: ok. Length: 537 nt. Measured usable bases: 265. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 265 | 0.2386 | 0.2307 |
| rnafold | ok | 265 | 0.1899 | 0.1771 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | 0.0308 | -0.0468 |
| seed_p | 73 | -0.3290 | -0.3282 |
| seed_p_vs_seed_pars | 62 | -0.4511 | -0.7140 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
