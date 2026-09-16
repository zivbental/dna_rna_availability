# YBR244W
Status: ok. Length: 649 nt. Measured usable bases: 337. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 337 | 0.3415 | 0.3200 |
| rnafold | ok | 337 | 0.3248 | 0.2862 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | 0.1742 | 0.1785 |
| seed_p | 92 | -0.3357 | -0.3458 |
| seed_p_vs_seed_pars | 73 | -0.0833 | -0.0338 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
