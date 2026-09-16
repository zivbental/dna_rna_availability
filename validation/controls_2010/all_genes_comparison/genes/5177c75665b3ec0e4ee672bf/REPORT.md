# YBR142W
Status: ok. Length: 2510 nt. Measured usable bases: 933. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 933 | 0.3647 | 0.3584 |
| rnafold | ok | 933 | 0.3541 | 0.3461 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | 0.4544 | -0.4306 |
| seed_p | 31 | -0.1318 | -0.2944 |
| seed_p_vs_seed_pars | 31 | -0.1492 | -0.5485 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
