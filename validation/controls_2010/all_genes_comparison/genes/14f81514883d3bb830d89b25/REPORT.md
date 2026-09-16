# YLR118C
Status: ok. Length: 800 nt. Measured usable bases: 506. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 506 | 0.2668 | 0.2502 |
| rnafold | ok | 506 | 0.1744 | 0.2009 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 241 | -0.1686 | -0.2403 |
| seed_p | 241 | -0.2259 | -0.2965 |
| seed_p_vs_seed_pars | 199 | -0.3241 | -0.2620 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
