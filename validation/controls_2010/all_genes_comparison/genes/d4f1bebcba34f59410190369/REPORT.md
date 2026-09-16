# YLR018C
Status: ok. Length: 1058 nt. Measured usable bases: 573. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 573 | 0.2339 | 0.2388 |
| rnafold | ok | 573 | 0.2566 | 0.2781 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | 0.2072 | 0.3850 |
| seed_p | 149 | 0.1022 | 0.1324 |
| seed_p_vs_seed_pars | 82 | 0.0430 | 0.0659 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
