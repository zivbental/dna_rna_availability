# YLR195C
Status: ok. Length: 1666 nt. Measured usable bases: 936. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 936 | 0.3723 | 0.3363 |
| rnafold | ok | 936 | 0.3385 | 0.3102 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 357 | -0.0340 | 0.0041 |
| seed_p | 357 | -0.0800 | 0.0504 |
| seed_p_vs_seed_pars | 243 | -0.0974 | -0.0042 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
