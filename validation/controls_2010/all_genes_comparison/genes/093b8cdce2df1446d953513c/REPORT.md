# YIR034C
Status: ok. Length: 1185 nt. Measured usable bases: 692. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 692 | 0.2830 | 0.2972 |
| rnafold | ok | 692 | 0.2302 | 0.2500 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 246 | -0.0002 | 0.1385 |
| seed_p | 246 | 0.0549 | 0.0327 |
| seed_p_vs_seed_pars | 208 | -0.2761 | -0.1577 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
