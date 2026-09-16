# YDR020C
Status: ok. Length: 1173 nt. Measured usable bases: 522. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 522 | 0.2730 | 0.2797 |
| rnafold | ok | 522 | 0.2056 | 0.2286 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | -0.1276 | 0.0574 |
| seed_p | 69 | 0.1071 | 0.2083 |
| seed_p_vs_seed_pars | 56 | 0.1750 | 0.3182 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
