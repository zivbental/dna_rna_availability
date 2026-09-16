# YHR024C
Status: ok. Length: 1713 nt. Measured usable bases: 842. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 842 | 0.3931 | 0.3788 |
| rnafold | ok | 842 | 0.2839 | 0.2898 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 211 | -0.3013 | -0.0953 |
| seed_p | 211 | -0.3746 | -0.3352 |
| seed_p_vs_seed_pars | 126 | -0.1833 | -0.1276 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
