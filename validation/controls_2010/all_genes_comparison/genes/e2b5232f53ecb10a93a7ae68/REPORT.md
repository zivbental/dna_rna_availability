# YDR434W
Status: ok. Length: 1819 nt. Measured usable bases: 1080. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1080 | 0.2286 | 0.2114 |
| rnafold | ok | 1080 | 0.2179 | 0.2068 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 424 | 0.0376 | -0.1773 |
| seed_p | 424 | -0.3525 | -0.3451 |
| seed_p_vs_seed_pars | 311 | -0.3857 | -0.4364 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
