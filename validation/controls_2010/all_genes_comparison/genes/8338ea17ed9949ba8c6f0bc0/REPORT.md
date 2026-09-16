# YPL058C
Status: ok. Length: 4915 nt. Measured usable bases: 2207. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2207 | 0.2697 | 0.2468 |
| rnafold | ok | 2207 | 0.2158 | 0.2015 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 329 | -0.2628 | -0.1800 |
| seed_p | 329 | -0.3708 | -0.2487 |
| seed_p_vs_seed_pars | 201 | -0.5782 | -0.4536 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
