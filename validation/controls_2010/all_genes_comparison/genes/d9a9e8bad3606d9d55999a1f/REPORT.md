# YLR069C
Status: ok. Length: 2447 nt. Measured usable bases: 892. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 892 | 0.2744 | 0.2569 |
| rnafold | ok | 892 | 0.2126 | 0.1990 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 90 | -0.0310 | 0.1965 |
| seed_p | 90 | -0.2904 | -0.2761 |
| seed_p_vs_seed_pars | 66 | -0.5040 | -0.4139 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
