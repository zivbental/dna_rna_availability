# YEL013W
Status: ok. Length: 1737 nt. Measured usable bases: 1201. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1201 | 0.3513 | 0.3378 |
| rnafold | ok | 1201 | 0.2963 | 0.2909 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 689 | -0.1373 | -0.0607 |
| seed_p | 689 | -0.0874 | -0.0514 |
| seed_p_vs_seed_pars | 547 | -0.2109 | -0.1631 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
