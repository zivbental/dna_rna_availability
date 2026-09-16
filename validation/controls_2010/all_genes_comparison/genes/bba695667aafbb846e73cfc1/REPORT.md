# YDL192W
Status: ok. Length: 641 nt. Measured usable bases: 469. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 469 | 0.2407 | 0.2132 |
| rnafold | ok | 469 | 0.2417 | 0.2189 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 354 | -0.1246 | -0.2404 |
| seed_p | 354 | -0.1594 | -0.1189 |
| seed_p_vs_seed_pars | 339 | -0.0254 | -0.1024 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
