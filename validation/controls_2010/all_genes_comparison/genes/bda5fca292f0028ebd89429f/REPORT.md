# YJL020C
Status: ok. Length: 3670 nt. Measured usable bases: 1401. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1401 | 0.3169 | 0.3060 |
| rnafold | ok | 1401 | 0.2714 | 0.2723 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 78 | -0.4363 | -0.4706 |
| seed_p | 78 | -0.2661 | -0.3501 |
| seed_p_vs_seed_pars | 66 | -0.3162 | -0.4900 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
