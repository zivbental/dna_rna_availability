# YGL001C
Status: ok. Length: 1207 nt. Measured usable bases: 978. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 978 | 0.3705 | 0.3656 |
| rnafold | ok | 978 | 0.3134 | 0.3247 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 790 | -0.1004 | -0.2573 |
| seed_p | 790 | -0.2872 | -0.2526 |
| seed_p_vs_seed_pars | 641 | -0.3634 | -0.2918 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
