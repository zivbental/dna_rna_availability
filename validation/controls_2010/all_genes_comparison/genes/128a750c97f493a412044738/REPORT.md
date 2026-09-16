# YHL017W
Status: ok. Length: 1804 nt. Measured usable bases: 1000. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1000 | 0.2283 | 0.2317 |
| rnafold | ok | 1000 | 0.1863 | 0.1931 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 341 | 0.1018 | 0.1860 |
| seed_p | 341 | 0.3285 | 0.3146 |
| seed_p_vs_seed_pars | 256 | 0.1246 | 0.0537 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
