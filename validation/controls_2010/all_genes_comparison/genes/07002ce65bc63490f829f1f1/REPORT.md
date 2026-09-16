# YJR085C
Status: ok. Length: 386 nt. Measured usable bases: 305. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 305 | 0.3334 | 0.3214 |
| rnafold | ok | 305 | 0.3303 | 0.3096 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 260 | -0.1395 | -0.0141 |
| seed_p | 260 | -0.2117 | -0.1668 |
| seed_p_vs_seed_pars | 235 | -0.0903 | -0.1624 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
