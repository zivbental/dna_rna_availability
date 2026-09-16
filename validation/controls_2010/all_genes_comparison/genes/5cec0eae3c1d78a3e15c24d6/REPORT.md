# YGR277C
Status: ok. Length: 990 nt. Measured usable bases: 518. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 518 | 0.3763 | 0.3776 |
| rnafold | ok | 518 | 0.3465 | 0.3473 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | -0.3447 | -0.5206 |
| seed_p | 149 | -0.2783 | -0.2458 |
| seed_p_vs_seed_pars | 133 | -0.4879 | -0.5693 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
