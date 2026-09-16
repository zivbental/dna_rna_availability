# YGR268C
Status: ok. Length: 749 nt. Measured usable bases: 338. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 338 | 0.3212 | 0.3229 |
| rnafold | ok | 338 | 0.2824 | 0.2808 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 52 | 0.3452 | 0.4345 |
| seed_p | 52 | -0.1770 | -0.4093 |
| seed_p_vs_seed_pars | 47 | -0.2747 | -0.4227 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
