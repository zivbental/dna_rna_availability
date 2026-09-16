# YLR286C
Status: ok. Length: 2067 nt. Measured usable bases: 1869. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1869 | 0.2854 | 0.2792 |
| rnafold | ok | 1869 | 0.2040 | 0.1981 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1791 | -0.2687 | -0.2592 |
| seed_p | 1791 | -0.2009 | -0.2017 |
| seed_p_vs_seed_pars | 1674 | -0.2621 | -0.2734 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
