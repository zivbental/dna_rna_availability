# YNR049C
Status: ok. Length: 785 nt. Measured usable bases: 321. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 321 | 0.3226 | 0.3408 |
| rnafold | ok | 321 | 0.3019 | 0.3313 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | 0.1464 | 0.3533 |
| seed_p | 31 | 0.2357 | 0.2820 |
| seed_p_vs_seed_pars | 20 | 0.5148 | 1.0000 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
