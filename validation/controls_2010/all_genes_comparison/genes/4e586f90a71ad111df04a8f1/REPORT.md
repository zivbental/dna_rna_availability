# YPR024W
Status: ok. Length: 2867 nt. Measured usable bases: 1848. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1848 | 0.3266 | 0.3115 |
| rnafold | ok | 1848 | 0.2875 | 0.2816 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 765 | 0.2171 | 0.0955 |
| seed_p | 765 | 0.0965 | 0.1463 |
| seed_p_vs_seed_pars | 559 | -0.0580 | 0.0384 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
