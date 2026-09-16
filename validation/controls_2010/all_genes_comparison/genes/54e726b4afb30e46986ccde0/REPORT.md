# YIL158W
Status: ok. Length: 744 nt. Measured usable bases: 283. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 283 | 0.4155 | 0.4154 |
| rnafold | ok | 283 | 0.3926 | 0.3763 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | -0.4188 | -0.4447 |
| seed_p | 50 | -0.2564 | -0.5782 |
| seed_p_vs_seed_pars | 27 | -0.1699 | -0.2715 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
