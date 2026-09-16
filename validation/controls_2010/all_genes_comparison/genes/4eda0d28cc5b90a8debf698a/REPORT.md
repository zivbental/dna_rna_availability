# YPL112C
Status: ok. Length: 1289 nt. Measured usable bases: 538. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 538 | 0.3023 | 0.3011 |
| rnafold | ok | 538 | 0.3165 | 0.3234 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 75 | -0.5593 | -0.5300 |
| seed_p | 75 | -0.1586 | -0.1160 |
| seed_p_vs_seed_pars | 38 | 0.0857 | -0.2530 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
