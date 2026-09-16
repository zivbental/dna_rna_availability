# YGL115W
Status: ok. Length: 1173 nt. Measured usable bases: 828. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 828 | 0.3459 | 0.3367 |
| rnafold | ok | 828 | 0.2753 | 0.2641 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 476 | 0.0082 | 0.0858 |
| seed_p | 476 | 0.0122 | 0.0180 |
| seed_p_vs_seed_pars | 406 | -0.0313 | -0.0593 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
