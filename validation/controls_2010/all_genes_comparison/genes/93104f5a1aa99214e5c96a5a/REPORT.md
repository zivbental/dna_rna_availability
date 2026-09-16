# YDL232W
Status: ok. Length: 419 nt. Measured usable bases: 277. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 277 | 0.2384 | 0.2789 |
| rnafold | ok | 277 | 0.2349 | 0.2390 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 176 | -0.1126 | 0.1318 |
| seed_p | 176 | -0.1590 | -0.3235 |
| seed_p_vs_seed_pars | 148 | -0.1014 | -0.3472 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
