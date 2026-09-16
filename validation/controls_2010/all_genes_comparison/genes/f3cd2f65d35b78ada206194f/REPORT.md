# YDR055W
Status: ok. Length: 1545 nt. Measured usable bases: 1007. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1007 | 0.2718 | 0.2654 |
| rnafold | ok | 1007 | 0.2313 | 0.2243 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 545 | -0.2220 | -0.2542 |
| seed_p | 545 | -0.3343 | -0.2866 |
| seed_p_vs_seed_pars | 430 | -0.3428 | -0.3211 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
