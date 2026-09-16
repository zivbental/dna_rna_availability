# YMR277W
Status: ok. Length: 2461 nt. Measured usable bases: 1150. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1150 | 0.3543 | 0.3436 |
| rnafold | ok | 1150 | 0.2772 | 0.2652 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 210 | 0.1075 | 0.1704 |
| seed_p | 210 | -0.0028 | 0.0379 |
| seed_p_vs_seed_pars | 134 | -0.3461 | 0.0268 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
