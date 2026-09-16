# YJR057W
Status: ok. Length: 741 nt. Measured usable bases: 312. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 312 | 0.3559 | 0.3818 |
| rnafold | ok | 312 | 0.2628 | 0.3267 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | -0.2110 | -0.2665 |
| seed_p | 49 | -0.5409 | -0.3554 |
| seed_p_vs_seed_pars | 39 | -0.6708 | -0.7782 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
