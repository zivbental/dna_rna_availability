# YNL255C
Status: ok. Length: 735 nt. Measured usable bases: 549. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 549 | 0.4258 | 0.4048 |
| rnafold | ok | 549 | 0.3744 | 0.3587 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 466 | -0.2566 | -0.2140 |
| seed_p | 466 | -0.4494 | -0.3354 |
| seed_p_vs_seed_pars | 436 | -0.5551 | -0.3507 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
