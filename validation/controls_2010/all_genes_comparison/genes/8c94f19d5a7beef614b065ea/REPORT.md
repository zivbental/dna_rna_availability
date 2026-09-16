# YMR214W
Status: ok. Length: 1333 nt. Measured usable bases: 830. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 830 | 0.3548 | 0.3502 |
| rnafold | ok | 830 | 0.2798 | 0.2652 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 435 | -0.1059 | 0.0964 |
| seed_p | 435 | -0.1514 | -0.0006 |
| seed_p_vs_seed_pars | 344 | 0.0143 | 0.0524 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
