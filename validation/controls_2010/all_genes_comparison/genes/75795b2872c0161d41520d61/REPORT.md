# YDL132W
Status: ok. Length: 2817 nt. Measured usable bases: 1246. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1246 | 0.2656 | 0.2651 |
| rnafold | ok | 1246 | 0.2334 | 0.2288 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 132 | -0.2494 | 0.0561 |
| seed_p | 132 | -0.3693 | -0.3951 |
| seed_p_vs_seed_pars | 107 | -0.6115 | -0.5304 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
