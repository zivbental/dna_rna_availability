# YER070W
Status: ok. Length: 2911 nt. Measured usable bases: 2393. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2393 | 0.2637 | 0.2599 |
| rnafold | ok | 2393 | 0.1951 | 0.2011 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2122 | -0.1006 | -0.1997 |
| seed_p | 2122 | -0.2544 | -0.2503 |
| seed_p_vs_seed_pars | 1798 | -0.4217 | -0.4301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
