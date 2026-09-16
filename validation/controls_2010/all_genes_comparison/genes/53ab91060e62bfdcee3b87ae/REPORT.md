# YGR117C
Status: ok. Length: 1830 nt. Measured usable bases: 770. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 770 | 0.2750 | 0.2692 |
| rnafold | ok | 770 | 0.2256 | 0.2059 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 86 | -0.0759 | 0.0764 |
| seed_p | 86 | -0.0672 | -0.3145 |
| seed_p_vs_seed_pars | 54 | -0.6810 | -0.5927 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
