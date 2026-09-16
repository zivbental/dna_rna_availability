# YDR320C-A
Status: ok. Length: 273 nt. Measured usable bases: 193. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 193 | 0.4390 | 0.4428 |
| rnafold | ok | 193 | 0.3957 | 0.3922 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 129 | -0.1384 | -0.6003 |
| seed_p | 129 | -0.0580 | -0.3054 |
| seed_p_vs_seed_pars | 105 | 0.1518 | -0.0978 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
