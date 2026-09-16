# YHL021C
Status: ok. Length: 1497 nt. Measured usable bases: 617. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 617 | 0.3010 | 0.3113 |
| rnafold | ok | 617 | 0.2441 | 0.2675 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 110 | -0.3199 | -0.2496 |
| seed_p | 110 | -0.4895 | -0.2306 |
| seed_p_vs_seed_pars | 63 | -0.4509 | -0.4390 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
