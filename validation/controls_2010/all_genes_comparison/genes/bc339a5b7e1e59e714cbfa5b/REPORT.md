# YAL035W
Status: ok. Length: 3134 nt. Measured usable bases: 1720. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1720 | 0.2885 | 0.2784 |
| rnafold | ok | 1720 | 0.2779 | 0.2813 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 746 | 0.0816 | -0.0639 |
| seed_p | 746 | -0.2388 | -0.1617 |
| seed_p_vs_seed_pars | 559 | -0.3405 | -0.2908 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
