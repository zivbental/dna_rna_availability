# YDL198C
Status: ok. Length: 1140 nt. Measured usable bases: 717. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 717 | 0.2784 | 0.2667 |
| rnafold | ok | 717 | 0.2313 | 0.2188 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 305 | 0.0299 | -0.3400 |
| seed_p | 305 | -0.2448 | -0.2006 |
| seed_p_vs_seed_pars | 253 | -0.3521 | -0.3664 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
