# YGR149W
Status: ok. Length: 1628 nt. Measured usable bases: 630. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 630 | 0.2976 | 0.2793 |
| rnafold | ok | 630 | 0.3008 | 0.2806 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | -0.7729 | -0.2128 |
| seed_p | 31 | -0.2998 | -0.0319 |
| seed_p_vs_seed_pars | 18 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
