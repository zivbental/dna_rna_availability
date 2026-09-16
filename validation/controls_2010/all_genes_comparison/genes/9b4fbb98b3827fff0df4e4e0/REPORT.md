# YIL002W-A
Status: ok. Length: 295 nt. Measured usable bases: 170. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 170 | 0.2538 | 0.2773 |
| rnafold | ok | 170 | 0.2176 | 0.2293 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | 0.0619 | 0.0285 |
| seed_p | 72 | 0.5467 | 0.1053 |
| seed_p_vs_seed_pars | 70 | -0.0597 | -0.2289 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
