# YLR043C
Status: ok. Length: 416 nt. Measured usable bases: 374. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 374 | 0.3893 | 0.3823 |
| rnafold | ok | 374 | 0.2950 | 0.3133 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 364 | -0.2532 | -0.6278 |
| seed_p | 364 | -0.4351 | -0.5388 |
| seed_p_vs_seed_pars | 333 | -0.4437 | -0.6377 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
