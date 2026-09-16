# YPL254W
Status: ok. Length: 1774 nt. Measured usable bases: 611. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 611 | 0.3249 | 0.3074 |
| rnafold | ok | 611 | 0.2525 | 0.2375 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | -0.3496 | -0.6302 |
| seed_p | 54 | -0.7004 | -0.6983 |
| seed_p_vs_seed_pars | 50 | -0.4666 | -0.4162 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
