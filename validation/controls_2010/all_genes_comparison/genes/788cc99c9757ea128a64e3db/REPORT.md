# YOR117W
Status: ok. Length: 1505 nt. Measured usable bases: 1014. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1014 | 0.3218 | 0.3147 |
| rnafold | ok | 1014 | 0.2755 | 0.2756 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 487 | -0.0857 | -0.0195 |
| seed_p | 487 | -0.1925 | -0.1548 |
| seed_p_vs_seed_pars | 387 | -0.2332 | -0.2653 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
