# YGL196W
Status: ok. Length: 1465 nt. Measured usable bases: 757. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 757 | 0.2861 | 0.2845 |
| rnafold | ok | 757 | 0.2424 | 0.2349 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 253 | -0.3545 | -0.1713 |
| seed_p | 253 | -0.5690 | -0.4801 |
| seed_p_vs_seed_pars | 178 | -0.4859 | -0.3764 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
