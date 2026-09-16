# YIL003W
Status: ok. Length: 1003 nt. Measured usable bases: 403. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 403 | 0.3555 | 0.3463 |
| rnafold | ok | 403 | 0.3568 | 0.3463 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 24 | 0.4603 | 0.6975 |
| seed_p | 24 | 0.8932 | 0.8359 |
| seed_p_vs_seed_pars | 14 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
