# YKL058W
Status: ok. Length: 747 nt. Measured usable bases: 459. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 459 | 0.2357 | 0.2230 |
| rnafold | ok | 459 | 0.2190 | 0.1948 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 292 | 0.1830 | 0.0486 |
| seed_p | 292 | 0.0620 | -0.1238 |
| seed_p_vs_seed_pars | 245 | -0.2287 | -0.2904 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
