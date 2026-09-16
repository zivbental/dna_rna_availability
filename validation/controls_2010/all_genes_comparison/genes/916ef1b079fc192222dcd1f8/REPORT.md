# YER131W
Status: ok. Length: 867 nt. Measured usable bases: 340. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 340 | 0.3219 | 0.3136 |
| rnafold | ok | 340 | 0.2023 | 0.2114 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 174 | 0.0469 | -0.1007 |
| seed_p | 174 | -0.2429 | -0.2439 |
| seed_p_vs_seed_pars | 162 | -0.2751 | -0.2896 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
