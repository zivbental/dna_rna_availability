# YER087C-B
Status: ok. Length: 470 nt. Measured usable bases: 375. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 375 | 0.2166 | 0.2083 |
| rnafold | ok | 375 | 0.1264 | 0.1031 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 297 | 0.0369 | -0.0201 |
| seed_p | 297 | -0.1286 | -0.1868 |
| seed_p_vs_seed_pars | 237 | -0.1322 | -0.1696 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
