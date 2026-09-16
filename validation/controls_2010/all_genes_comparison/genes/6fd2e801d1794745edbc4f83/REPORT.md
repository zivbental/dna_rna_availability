# YKL100C
Status: ok. Length: 1875 nt. Measured usable bases: 1119. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1119 | 0.2825 | 0.2728 |
| rnafold | ok | 1119 | 0.2039 | 0.2158 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 460 | 0.1327 | 0.0637 |
| seed_p | 460 | -0.0976 | -0.0771 |
| seed_p_vs_seed_pars | 314 | -0.0273 | -0.0307 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
