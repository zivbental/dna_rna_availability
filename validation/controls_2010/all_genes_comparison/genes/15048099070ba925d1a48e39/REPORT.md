# YDR400W
Status: ok. Length: 1380 nt. Measured usable bases: 637. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 637 | 0.3618 | 0.3441 |
| rnafold | ok | 637 | 0.3496 | 0.3301 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 184 | -0.4618 | -0.3274 |
| seed_p | 184 | -0.5237 | -0.4020 |
| seed_p_vs_seed_pars | 135 | -0.6580 | -0.6008 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
