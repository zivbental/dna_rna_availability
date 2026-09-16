# YLR429W
Status: ok. Length: 2040 nt. Measured usable bases: 1383. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1383 | 0.2848 | 0.2698 |
| rnafold | ok | 1383 | 0.2843 | 0.2727 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 767 | 0.0277 | 0.0374 |
| seed_p | 767 | 0.0979 | 0.1161 |
| seed_p_vs_seed_pars | 527 | -0.0244 | 0.1564 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
