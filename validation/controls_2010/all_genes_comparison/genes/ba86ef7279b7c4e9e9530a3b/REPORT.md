# YOL022C
Status: ok. Length: 1330 nt. Measured usable bases: 774. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 774 | 0.3494 | 0.3358 |
| rnafold | ok | 774 | 0.3576 | 0.3380 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 210 | 0.2091 | 0.1823 |
| seed_p | 210 | 0.1151 | 0.1201 |
| seed_p_vs_seed_pars | 140 | -0.1830 | -0.1252 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
