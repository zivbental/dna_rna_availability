# YLR016C
Status: ok. Length: 790 nt. Measured usable bases: 368. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 368 | 0.3421 | 0.3279 |
| rnafold | ok | 368 | 0.1632 | 0.1246 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 155 | -0.2810 | -0.2007 |
| seed_p | 155 | -0.4729 | -0.4006 |
| seed_p_vs_seed_pars | 113 | -0.7926 | -0.7049 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
