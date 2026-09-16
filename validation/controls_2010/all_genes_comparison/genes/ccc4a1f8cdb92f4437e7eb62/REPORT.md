# YJL042W
Status: ok. Length: 4398 nt. Measured usable bases: 1783. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1783 | 0.3063 | 0.2968 |
| rnafold | ok | 1783 | 0.2508 | 0.2428 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | -0.3812 | -0.5397 |
| seed_p | 153 | -0.5237 | -0.5401 |
| seed_p_vs_seed_pars | 94 | -0.4742 | -0.4174 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
