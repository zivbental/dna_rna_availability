# YOR087W
Status: ok. Length: 2128 nt. Measured usable bases: 1008. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1008 | 0.2627 | 0.2692 |
| rnafold | ok | 1008 | 0.2261 | 0.2371 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 251 | -0.0297 | -0.2618 |
| seed_p | 251 | -0.3160 | -0.3285 |
| seed_p_vs_seed_pars | 192 | -0.3666 | -0.4675 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
