# YGL200C
Status: ok. Length: 744 nt. Measured usable bases: 675. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 675 | 0.2868 | 0.2948 |
| rnafold | ok | 675 | 0.2475 | 0.2332 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 667 | 0.0564 | -0.1597 |
| seed_p | 667 | -0.1289 | -0.2570 |
| seed_p_vs_seed_pars | 611 | -0.2928 | -0.3622 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
