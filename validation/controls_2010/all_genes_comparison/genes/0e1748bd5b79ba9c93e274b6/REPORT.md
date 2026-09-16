# YIL121W
Status: ok. Length: 1833 nt. Measured usable bases: 992. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 992 | 0.2877 | 0.2758 |
| rnafold | ok | 992 | 0.3194 | 0.2936 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 363 | -0.0953 | -0.1754 |
| seed_p | 363 | -0.3448 | -0.3911 |
| seed_p_vs_seed_pars | 272 | -0.5665 | -0.5150 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
