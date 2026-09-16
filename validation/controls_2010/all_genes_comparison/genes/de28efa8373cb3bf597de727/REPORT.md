# YKL156W
Status: ok. Length: 468 nt. Measured usable bases: 400. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 400 | 0.3346 | 0.3290 |
| rnafold | ok | 400 | 0.2747 | 0.2940 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 358 | -0.3098 | -0.4524 |
| seed_p | 358 | -0.3983 | -0.3920 |
| seed_p_vs_seed_pars | 352 | -0.3737 | -0.3647 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
