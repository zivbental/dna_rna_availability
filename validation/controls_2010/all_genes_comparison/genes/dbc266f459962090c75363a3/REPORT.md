# YDL213C
Status: ok. Length: 745 nt. Measured usable bases: 310. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 310 | 0.3990 | 0.3928 |
| rnafold | ok | 310 | 0.4085 | 0.4245 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | -0.4713 | -0.6570 |
| seed_p | 73 | -0.8471 | -0.8298 |
| seed_p_vs_seed_pars | 53 | -0.9089 | -0.9338 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
