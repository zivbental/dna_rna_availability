# YCR087C-A
Status: ok. Length: 648 nt. Measured usable bases: 307. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 307 | 0.2794 | 0.3035 |
| rnafold | ok | 307 | 0.1558 | 0.1567 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 102 | -0.0886 | -0.1988 |
| seed_p | 102 | -0.2852 | -0.2127 |
| seed_p_vs_seed_pars | 86 | -0.2891 | -0.1271 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
