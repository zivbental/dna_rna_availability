# YKL053C-A
Status: ok. Length: 424 nt. Measured usable bases: 238. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 238 | 0.4099 | 0.3974 |
| rnafold | ok | 238 | 0.3962 | 0.3730 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 84 | -0.3837 | -0.7642 |
| seed_p | 84 | -0.5987 | -0.6701 |
| seed_p_vs_seed_pars | 73 | -0.7717 | -0.6700 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
