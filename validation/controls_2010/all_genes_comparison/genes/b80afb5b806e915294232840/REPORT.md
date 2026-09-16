# YDL173W
Status: ok. Length: 1060 nt. Measured usable bases: 452. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 452 | 0.2735 | 0.2766 |
| rnafold | ok | 452 | 0.2471 | 0.2522 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 68 | 0.3991 | 0.7903 |
| seed_p | 68 | 0.5469 | 0.5660 |
| seed_p_vs_seed_pars | 47 | 0.5067 | 0.5207 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
