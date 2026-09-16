# YFR005C
Status: ok. Length: 1573 nt. Measured usable bases: 707. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 707 | 0.3181 | 0.2966 |
| rnafold | ok | 707 | 0.3448 | 0.3266 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | -0.1328 | -0.6236 |
| seed_p | 101 | -0.1933 | -0.2746 |
| seed_p_vs_seed_pars | 62 | -0.5843 | -0.5437 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
