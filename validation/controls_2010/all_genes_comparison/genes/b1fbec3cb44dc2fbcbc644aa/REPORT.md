# YDL165W
Status: ok. Length: 662 nt. Measured usable bases: 381. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 381 | 0.2208 | 0.2352 |
| rnafold | ok | 381 | 0.1869 | 0.2082 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | -0.4218 | -0.3612 |
| seed_p | 135 | -0.0751 | -0.1445 |
| seed_p_vs_seed_pars | 113 | -0.2735 | -0.2880 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
