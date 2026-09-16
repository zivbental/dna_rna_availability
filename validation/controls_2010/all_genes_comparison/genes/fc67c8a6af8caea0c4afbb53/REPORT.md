# YDR322C-A
Status: ok. Length: 508 nt. Measured usable bases: 249. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 249 | 0.3168 | 0.3173 |
| rnafold | ok | 249 | 0.2880 | 0.3385 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 68 | 0.0165 | 0.1107 |
| seed_p | 68 | -0.5607 | -0.5876 |
| seed_p_vs_seed_pars | 63 | -0.8112 | -0.7018 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
