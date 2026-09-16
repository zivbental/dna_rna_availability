# YKR030W
Status: ok. Length: 962 nt. Measured usable bases: 388. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 388 | 0.1520 | 0.1654 |
| rnafold | ok | 388 | 0.1067 | 0.1255 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | -0.5290 | -0.8678 |
| seed_p | 77 | -0.5434 | -0.3438 |
| seed_p_vs_seed_pars | 58 | 0.4049 | 0.5218 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
