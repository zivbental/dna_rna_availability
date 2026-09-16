# YGL100W
Status: ok. Length: 1162 nt. Measured usable bases: 729. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 729 | 0.4253 | 0.4134 |
| rnafold | ok | 729 | 0.4260 | 0.4041 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 403 | -0.2744 | -0.4660 |
| seed_p | 403 | -0.2670 | -0.3738 |
| seed_p_vs_seed_pars | 319 | -0.3552 | -0.4592 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
