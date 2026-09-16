# YLR022C
Status: ok. Length: 802 nt. Measured usable bases: 432. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 432 | 0.3298 | 0.3395 |
| rnafold | ok | 432 | 0.2360 | 0.2501 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 162 | -0.0723 | -0.1536 |
| seed_p | 162 | -0.1422 | -0.2686 |
| seed_p_vs_seed_pars | 129 | -0.0550 | -0.1254 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
