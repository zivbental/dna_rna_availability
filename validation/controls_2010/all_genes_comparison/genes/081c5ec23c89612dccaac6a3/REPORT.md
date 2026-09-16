# YOL102C
Status: ok. Length: 834 nt. Measured usable bases: 305. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 305 | 0.3984 | 0.3941 |
| rnafold | ok | 305 | 0.2433 | 0.2207 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 15 | undefined | undefined |
| seed_p | 15 | undefined | undefined |
| seed_p_vs_seed_pars | 9 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
