# YGL242C
Status: ok. Length: 689 nt. Measured usable bases: 403. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 403 | 0.4178 | 0.3934 |
| rnafold | ok | 403 | 0.3605 | 0.3377 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 165 | 0.2743 | 0.5143 |
| seed_p | 165 | 0.2833 | 0.1760 |
| seed_p_vs_seed_pars | 125 | 0.3069 | 0.1986 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
