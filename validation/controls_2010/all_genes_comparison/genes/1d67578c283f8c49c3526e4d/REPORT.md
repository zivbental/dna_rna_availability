# YHR110W
Status: ok. Length: 763 nt. Measured usable bases: 517. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 517 | 0.3525 | 0.3515 |
| rnafold | ok | 517 | 0.3118 | 0.3288 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 314 | -0.0664 | 0.2016 |
| seed_p | 314 | -0.0057 | 0.0259 |
| seed_p_vs_seed_pars | 217 | -0.1670 | -0.2758 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
