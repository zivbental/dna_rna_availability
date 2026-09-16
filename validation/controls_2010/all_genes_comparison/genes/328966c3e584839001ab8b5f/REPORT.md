# YJR069C
Status: ok. Length: 755 nt. Measured usable bases: 338. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 338 | 0.3436 | 0.3439 |
| rnafold | ok | 338 | 0.3179 | 0.3324 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 125 | 0.3268 | 0.5102 |
| seed_p | 125 | -0.2921 | -0.1690 |
| seed_p_vs_seed_pars | 109 | -0.5393 | -0.5143 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
