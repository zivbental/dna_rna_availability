# YOL086C
Status: ok. Length: 1154 nt. Measured usable bases: 706. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 706 | 0.3295 | 0.3211 |
| rnafold | ok | 706 | 0.3104 | 0.3203 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 555 | 0.0771 | -0.0443 |
| seed_p | 555 | -0.0376 | -0.0655 |
| seed_p_vs_seed_pars | 505 | -0.1377 | -0.1524 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
