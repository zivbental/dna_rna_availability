# YGR241C
Status: ok. Length: 1856 nt. Measured usable bases: 731. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 731 | 0.2976 | 0.2922 |
| rnafold | ok | 731 | 0.2590 | 0.2448 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 93 | -0.2845 | -0.1840 |
| seed_p | 93 | -0.1827 | -0.1469 |
| seed_p_vs_seed_pars | 71 | -0.2919 | -0.3406 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
