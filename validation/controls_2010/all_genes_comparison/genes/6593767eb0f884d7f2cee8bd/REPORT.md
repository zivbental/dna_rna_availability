# YBR210W
Status: ok. Length: 672 nt. Measured usable bases: 278. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 278 | 0.2167 | 0.1910 |
| rnafold | ok | 278 | 0.2032 | 0.1650 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | -0.6034 | -0.8908 |
| seed_p | 34 | 0.5202 | 0.4832 |
| seed_p_vs_seed_pars | 31 | -0.0735 | -0.1023 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
