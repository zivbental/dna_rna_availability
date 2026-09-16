# YIL125W
Status: ok. Length: 3258 nt. Measured usable bases: 1413. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1413 | 0.3338 | 0.3314 |
| rnafold | ok | 1413 | 0.2527 | 0.2567 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 151 | 0.0084 | 0.4094 |
| seed_p | 151 | 0.4383 | 0.5749 |
| seed_p_vs_seed_pars | 108 | 0.1656 | 0.3690 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
