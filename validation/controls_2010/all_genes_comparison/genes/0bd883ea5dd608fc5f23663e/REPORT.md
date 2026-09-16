# YLR292C
Status: ok. Length: 735 nt. Measured usable bases: 475. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 475 | 0.3672 | 0.3725 |
| rnafold | ok | 475 | 0.3708 | 0.3736 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 232 | -0.0503 | -0.0684 |
| seed_p | 232 | -0.2945 | -0.3374 |
| seed_p_vs_seed_pars | 172 | -0.2746 | -0.2806 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
