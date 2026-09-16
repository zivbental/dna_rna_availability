# YBR251W
Status: ok. Length: 1044 nt. Measured usable bases: 448. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 448 | 0.4306 | 0.4195 |
| rnafold | ok | 448 | 0.4298 | 0.4308 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 56 | -0.8199 | -0.7710 |
| seed_p | 56 | -0.6581 | -0.6639 |
| seed_p_vs_seed_pars | 48 | -0.8182 | -0.6007 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
